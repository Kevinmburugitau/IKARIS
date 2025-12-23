#!/usr/bin/env python3
"""
texas_holdem.py
Simple Texas Hold'em CLI simulator.

Features:
- 2..6 players (human + CPU or all CPU)
- Deal hole cards, flop, turn, river
- Evaluate best 5-card poker hand per player and determine winner(s)
- Play multiple rounds, reshuffle each round
- Clear, commented code explaining each part

Usage:
  python texas_holdem.py
"""

import random
import itertools
import sys

# ---- Card and deck utilities ----

RANKS = "23456789TJQKA"                       # rank order low->high
SUITS = "CDHS"                                # clubs, diamonds, hearts, spades

def make_deck():
    """Return a new list of 52 card strings like 'Ah', 'TC', '5D' where rank+suit."""
    return [r + s for r in RANKS for s in SUITS]

def shuffle_deck(deck):
    """Shuffle deck in place using random.shuffle for unbiased random order."""
    random.shuffle(deck)

def card_rank_value(card):
    """Return numeric rank index for sorting/comparison (0..12)."""
    return RANKS.index(card[0])

# ---- Hand evaluator ----

# Hand categories ranked high->low for comparison: higher number = better hand
HAND_RANKS = {
    "Straight Flush": 8,
    "Four of a Kind": 7,
    "Full House": 6,
    "Flush": 5,
    "Straight": 4,
    "Three of a Kind": 3,
    "Two Pair": 2,
    "One Pair": 1,
    "High Card": 0
}

def group_by_rank(cards):
    """Return dict: rank_char -> list of cards with that rank."""
    d = {}
    for c in cards:
        d.setdefault(c[0], []).append(c)
    return d

def is_flush(cards):
    """Return (True, sorted_ranks) if any 5-card flush exists; sorted_ranks high->low returned for kicker tiebreaks."""
    suits = {}
    for c in cards:
        suits.setdefault(c[1], []).append(c)
    for suit, scards in suits.items():
        if len(scards) >= 5:
            # sort the flush cards by rank descending
            sorted_r = sorted(scards, key=lambda x: card_rank_value(x), reverse=True)
            return True, [card_rank_value(c) for c in sorted_r]
    return False, []

def is_straight(cards):
    """Return (True, high_rank_index) if any straight exists among cards (Ace can be low)."""
    # unique ranks only
    ranks = sorted({card_rank_value(c) for c in cards})
    if not ranks:
        return False, None
    # handle Ace-low straight by appending -1 for Ace as rank -1? easier: map Ace (12) to -1 when needed
    # Build list with duplicate Ace-low possibility
    rset = set(ranks)
    # check sequences of length 5
    for high in range(12, 3, -1):  # high = index of top card (12 down to 4)
        sequence = [(high - i) for i in range(5)]
        if all(x in rset for x in sequence):
            return True, high
    # wheel straight A-2-3-4-5: ranks indices 12,0,1,2,3
    if {12, 0, 1, 2, 3}.issubset(rset):
        return True, 3  # treat 5 as high (index 3)
    return False, None

def evaluate_7cards(cards):
    """
    Given 7 (or fewer) cards, return a tuple (category_rank, tiebreaker_list)
    Higher tuple compares as better hand.
    tiebreaker_list contains integers (rank indices) to break ties in order.
    """
    # Ensure card list length between 5 and 7
    if len(cards) < 5:
        raise ValueError("Need at least 5 cards to evaluate a hand")
    ranks_group = group_by_rank(cards)
    counts = sorted(((len(v), RANKS.index(k), k) for k,v in ranks_group.items()), reverse=True)
    # counts sorted by (count, rank_index, rank_char)
    # Check for flush and straight (straight flush requires both)
    flush, flush_ranks = is_flush(cards)
    straight, straight_high = is_straight(cards)
    # Check straight flush by filtering flush suit cards and checking straight on them
    if flush:
        # find suit with flush
        suit_cards = []
        suits = {}
        for c in cards:
            suits.setdefault(c[1], []).append(c)
        chosen_suit = None
        for s, sc in suits.items():
            if len(sc) >= 5:
                chosen_suit = s
                suit_cards = sc
                break
        sf, sf_high = is_straight(suit_cards)
        if sf:
            return (HAND_RANKS["Straight Flush"], [sf_high])
    # Four of a Kind
    if counts[0][0] == 4:
        four_rank = counts[0][1]
        # kicker: highest remaining rank
        kickers = sorted((card_rank_value(c) for c in cards if card_rank_value(c) != four_rank), reverse=True)
        return (HAND_RANKS["Four of a Kind"], [four_rank, kickers[0]])
    # Full House: a three + a pair (note: if multiple threes, one acts as pair)
    if counts[0][0] == 3 and any(c[0] >= 2 for c in counts[1:]):
        three_rank = counts[0][1]
        # find highest pair (or other three) rank
        pair_rank = max((c[1] for c in counts[1:] if c[0] >= 2))
        return (HAND_RANKS["Full House"], [three_rank, pair_rank])
    # Flush
    if flush:
        # top 5 ranks of flush suit as tiebreakers
        top5 = flush_ranks[:5]
        return (HAND_RANKS["Flush"], top5)
    # Straight
    if straight:
        return (HAND_RANKS["Straight"], [straight_high])
    # Three of a Kind
    if counts[0][0] == 3:
        three_rank = counts[0][1]
        # two highest kickers excluding three_rank
        kickers = sorted((card_rank_value(c) for c in cards if card_rank_value(c) != three_rank), reverse=True)[:2]
        return (HAND_RANKS["Three of a Kind"], [three_rank] + kickers)
    # Two Pair
    pairs = [c for c in counts if c[0] == 2]
    if len(pairs) >= 2:
        top_two = sorted((p[1] for p in pairs), reverse=True)[:2]
        kicker = max((card_rank_value(c) for c in cards if card_rank_value(c) not in top_two))
        return (HAND_RANKS["Two Pair"], top_two + [kicker])
    # One Pair
    if pairs:
        pair_rank = pairs[0][1]
        kickers = sorted((card_rank_value(c) for c in cards if card_rank_value(c) != pair_rank), reverse=True)[:3]
        return (HAND_RANKS["One Pair"], [pair_rank] + kickers)
    # High Card
    top5 = sorted((card_rank_value(c) for c in cards), reverse=True)[:5]
    return (HAND_RANKS["High Card"], top5)

def compare_hand_tuples(a, b):
    """Compare two evaluation tuples (category_rank, tiebreaker_list). Return 1 if a>b, -1 if a<b, 0 tie."""
    if a[0] != b[0]:
        return 1 if a[0] > b[0] else -1
    # compare tiebreaker lists lexicographically
    for x, y in itertools.zip_longest(a[1], b[1], fillvalue=-1):
        if x != y:
            return 1 if x > y else -1
    return 0

# ---- Game flow and I/O ----

def deal_hole_cards(deck, num_players):
    """Deal two hole cards to each player from deck; return list of lists."""
    hands = []
    for _ in range(num_players):
        hands.append([deck.pop(), deck.pop()])
    return hands

def deal_community(deck):
    """Deal flop(3), turn(1), river(1) returning list of community cards (5)."""
    # Burn before flop, turn, river typical in casino dealing; we emulate simple dealing without burns
    flop = [deck.pop(), deck.pop(), deck.pop()]
    turn = deck.pop()
    river = deck.pop()
    return flop + [turn, river]

def pretty(card):
    """Return human-friendly card representation, e.g., 'A♠'."""
    suit_map = {'C':'♣','D':'♦','H':'♥','S':'♠'}
    rank = card[0]
    suit = suit_map.get(card[1], card[1])
    return rank + suit

def show_table(hands, community, reveal_all=False):
    """Print current hands and community. If reveal_all False, only show CPU as 'XX' to hide hole cards when desired."""
    for i, h in enumerate(hands, 1):
        print(f"Player {i}:", ' '.join(pretty(c) for c in h))
    if community:
        print("Community:", ' '.join(pretty(c) for c in community))
    else:
        print("Community: (not dealt)")

def best_hand_for_player(hole, community):
    """Return evaluation tuple and the best 5-card combination (as list of card strings)."""
    all_cards = hole + community
    best_eval = None
    best_combo = None
    # iterate all 5-card combinations from available cards and evaluate
    for combo in itertools.combinations(all_cards, 5):
        ev = evaluate_7cards(list(combo))
        if best_eval is None or compare_hand_tuples(ev, best_eval) == 1:
            best_eval = ev
            best_combo = combo
    return best_eval, best_combo

def eval_name_from_rank(rank_num):
    """Get hand category name by rank number."""
    for k,v in HAND_RANKS.items():
        if v == rank_num:
            return k
    return "Unknown"

def play_round(num_players):
    """Play one round: shuffle, deal, showdown, and print winner(s)."""
    deck = make_deck()
    shuffle_deck(deck)
    hands = deal_hole_cards(deck, num_players)
    community = deal_community(deck)
    print("\n--- New round ---")
    for i, h in enumerate(hands, 1):
        print(f"Player {i} hole: {pretty(h[0])} {pretty(h[1])}")
    print("Community cards:", ' '.join(pretty(c) for c in community))
    # Evaluate each player's best hand
    evaluations = []
    for i, h in enumerate(hands, 1):
        ev, combo = best_hand_for_player(h, community)
        evaluations.append((i, ev, combo))
        catname = eval_name_from_rank(ev[0])
        print(f"Player {i}: {catname}, tiebreakers {ev[1]}, best 5: {' '.join(pretty(c) for c in combo)}")
    # Determine winner(s)
    # find best evaluation tuple
    evaluations_sorted = sorted(evaluations, key=lambda x: (x[1][0], x[1][1]), reverse=True)
    best_ev = evaluations_sorted[0][1]
    winners = [t[0] for t in evaluations if compare_hand_tuples(t[1], best_ev) == 0]
    if len(winners) == 1:
        print(f"Winner: Player {winners[0]}")
    else:
        print("Tie between players:", ', '.join(str(w) for w in winners))

# ---- Main interactive loop ----

def ask_int(prompt, minv, maxv):
    """Prompt for integer in range with loop on invalid input."""
    while True:
        try:
            val = int(input(prompt).strip())
            if val < minv or val > maxv:
                print(f"Please enter a number between {minv} and {maxv}.")
                continue
            return val
        except ValueError:
            print("Invalid input, please enter a number.")

def main():
    print("Simple Texas Hold'em simulator")
    num_players = ask_int("Number of players (2-6): ", 2, 6)
    while True:
        play_round(num_players)
        ans = input("\nPlay another round? (y/n): ").strip().lower()
        if ans and ans[0] == 'y':
            continue
        break
    print("Goodbye!")

if __name__ == "__main__":
    main()
