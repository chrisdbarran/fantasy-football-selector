from csp import Constraint, CSP
from typing import Dict, List, Optional

import csv
import logging

logging.basicConfig(filename='ff.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Player:

    def __init__(self, position: str, name: str, team: str, points: int, price: float, value: int):
        self.position = position
        self.name = name
        self.team = team
        self.points = points
        self.price = price
        self.value = value

    def __repr__(self) -> str:
        return f"{self.position} {self.name} {self.team} {self.points} {self.price}"

    def __dict__(self) -> dict:
        return {'position': self.position,
                 'name': self.name,
                  'team': self.team,
                  'points': self.points,
                  'price': self.price,
                  'value': self.value }

    def to_dict(p):
        return {'position': p.position,
                'name': p.name,
                'team': p.team,
                'points': p.points,
                'price': p.price,
                'value': p.value }

    def from_json(d):
        player = Player(d['position'],d['name'],d['team'], int(d['points']),float(d['price']),int(d['value'])) 
        return player

class FantasyFootballConstraint(Constraint[str, Player]):

    def __init__(self, positions: List[str]) -> None:
        super().__init__(positions)
        self.positions: List[str] = positions

    def satisfied(self, assignment: Dict[str, Player]) -> bool:
        # If there are duplicate values then it's not a soln       
        if len(set(assignment.values())) < len(assignment):
            return False

        if  self.more_than_three_from_one_team(assignment):
            return False

        # If the total cost is > £100M then it's not a solution
        if self.cost_over_one_hundred(assignment):
            return False

        
        if len(assignment) == len(self.positions):
            assignment_score = 0
            for position, player in assignment.items():
                assignment_score += player.points


            # Score of my team
            if assignment_score < target_score:
                return False

        return True

    def def_over_six(self, assignment: Dict[str, Player]) -> bool:
        for position, player in assignment.items():
            if player.position == "DEF":
                if player.price > 6.0:
                    return True
        return False

    def position_limit(self, assignment: Dict[str, Player], position: str, limit: float) -> bool:
        total_cost = 0
        for pos, player in assignment.items():
            if player.position == position:
                total_cost += player.price
        return total_cost > limit

    def cost_over_one_hundred(self, assignment: Dict[str, Player]) -> bool:
        # Add up the total cost
        total_cost: float = 0.0
        for player in assignment.values():
            total_cost += player.price
        return total_cost > 100.0

    def more_than_three_from_one_team(self, assignment: Dict[str,Player]) -> bool:

        team_selection_count = {}

        for player in assignment.values():
        # If element exists in dict then increment its value else add it in dict
            if player.team in team_selection_count:
                team_selection_count[player.team] += 1
            else:
                team_selection_count[player.team] = 1

        if max(team_selection_count.values()) > 3:
            return True
        return False


def load_players(position: str) -> List[Player]:
    players: List[Player] = []

    with open('players3.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if position == row[0]:
                player = Player(row[0], row[1], row[2], int(row[3]), float(row[4]), int(row[5]))
                players.append(player)
    
    return players

target_score = 2400

if __name__ == "__main__":

    
    
    # The Variables - THis controls order of picks
    positions: List[str] = [ "GK1", "GK2",
                            "DEF1", "DEF2", "DEF3",  "DEF4", "DEF5",
                             "MID1", "MID2", "MID3", "MID4", "MID5",
                             "FWD1","FWD2", "FWD3"
                            ]

    # The domains
    possible_selections: Dict[str, List[Player]] = {}

    list_of_keepers = load_players("GK")
    list_of_defenders = load_players("DEF")
    list_of_midfielders = load_players("MID")
    list_of_forwards = load_players("FWD")

    possible_selections["GK1"] = list_of_keepers
    possible_selections["GK2"] = list_of_keepers
    possible_selections["DEF1"] = list_of_defenders
    possible_selections["DEF2"] = list_of_defenders
    possible_selections["DEF3"] = list_of_defenders
    possible_selections["DEF4"] = list_of_defenders
    possible_selections["DEF5"] = list_of_defenders
    possible_selections["MID1"] = list_of_midfielders
    possible_selections["MID2"] = list_of_midfielders
    possible_selections["MID3"] = list_of_midfielders
    possible_selections["MID4"] = list_of_midfielders
    possible_selections["MID5"] = list_of_midfielders
    possible_selections["FWD1"] = list_of_forwards
    possible_selections["FWD2"] = list_of_forwards
    possible_selections["FWD3"] = list_of_forwards

    csp: CSP[str,Player] = CSP(positions, possible_selections)

    csp.add_constraint(FantasyFootballConstraint(positions))


    solution: Optional[Dict[str,Player]] = csp.backtracking_search()

    if solution is None:
        print("No solution found!")
    else:
        total_points = 0
        total_price = 0.0

        for position, player in solution.items():
            total_points += player.points
            total_price += player.price
            print(f"{position} {player}")

        print(f"\nTotal Points: {total_points}")
        print(f"Total Cost: {total_price}\n")

