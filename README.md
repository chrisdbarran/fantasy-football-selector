# FF Constraint problem

Using constraint solver from https://freecontent.manning.com/constraint-satisfaction-problems-in-python/ to pick a fantasy football team.

## Variables

The variables are the team positions to be filled.

e.g. GK1, GK2, DEF1,DEF2 ....

## Domains

The domains for a variable are the players that can be selected for a particular position.

e.g.  Only goal keepers are eligible for goal keeper positions

So there will be four distinct domains, the list of goalkeepers, defenders, midfielders and forwards.

## Constraints

1. You can only select a player once.
2. Only three players from one team in the whole selection.
3. Total cost may not exceed £100M.

## Thoughts on maximum value

1. Total points based on last years score.
2. Total points from last year divided by price
3. ICT Rank?

## Implementation

Would probably need to model the player as an Object.

class Player

  __init(self, name, team, price, points, ict)

Also, 

Implement the Constraint as one class that checks all the conditions.

Also, could create a condition that the total or the rank needs to be over a certain threshold.

So could run it once, find the total. Set that as a bar to be beaten, run it again. Keep going until the bar can't be beaten.

## Example teams generated.

```
GK1 GK Martínez Aston Villa 186 5.5
GK2 GK Meslier Leeds 154 5.0
DEF1 DEF Cresswell West Ham 153 5.5
DEF2 DEF Targett Aston Villa 138 5.0
DEF3 DEF Wan-Bissaka Man Utd 144 5.5
DEF4 DEF Dunk Brighton 130 5.0
DEF5 DEF Mings Aston Villa 128 5.0
MID1 MID Dallas Leeds 171 5.5
MID2 MID Harrison Leeds 160 6.0
MID3 MID Soucek West Ham 147 6.0
MID4 MID Ward-Prowse Southampton 156 6.5
MID5 MID Son Spurs 228 10.0
FWD1 FWD Calvert-Lewin Everton 165 8.0
FWD2 FWD Wood Burnley 138 7.0
FWD3 FWD Kane Spurs 242 12.5

Total Points: 2440
Total Cost: 98.0


GK1 GK Martínez Aston Villa 186 5.5
GK2 GK Meslier Leeds 154 5.0
DEF1 DEF Cresswell West Ham 153 5.5
DEF2 DEF Targett Aston Villa 138 5.0
DEF3 DEF Wan-Bissaka Man Utd 144 5.5
DEF4 DEF Dunk Brighton 130 5.0
DEF5 DEF Mings Aston Villa 128 5.0
MID1 MID Dallas Leeds 171 5.5
MID2 MID Harrison Leeds 160 6.0
MID3 MID Soucek West Ham 147 6.0
MID4 MID Ward-Prowse Southampton 156 6.5
MID5 MID Son Spurs 228 10.0
FWD1 FWD Calvert-Lewin Everton 165 8.0
FWD2 FWD Kane Spurs 242 12.5
FWD3 FWD Firmino Liverpool 141 9.0

Total Points: 2443
Total Cost: 100.0

GK1 GK Martínez Aston Villa 186 5.5
GK2 GK Meslier Leeds 154 5.0
DEF1 DEF Cresswell West Ham 153 5.5
DEF2 DEF Targett Aston Villa 138 5.0
DEF3 DEF Wan-Bissaka Man Utd 144 5.5
DEF4 DEF Dunk Brighton 130 5.0
DEF5 DEF Mings Aston Villa 128 5.0
MID1 MID Dallas Leeds 171 5.5
MID2 MID Harrison Leeds 160 6.0
MID3 MID Soucek West Ham 147 6.0
MID4 MID Ward-Prowse Southampton 156 6.5
MID5 MID Fernandes Man Utd 244 12.0
FWD1 FWD Calvert-Lewin Everton 165 8.0
FWD2 FWD Wood Burnley 138 7.0
FWD3 FWD Kane Spurs 242 12.5

Total Points: 2456
Total Cost: 100.0

GK1 GK Martínez Aston Villa 186 5.5
GK2 GK Meslier Leeds 154 5.0
DEF1 DEF Cresswell West Ham 153 5.5
DEF2 DEF Targett Aston Villa 138 5.0
DEF3 DEF Wan-Bissaka Man Utd 144 5.5
DEF4 DEF Dunk Brighton 130 5.0
DEF5 DEF Mings Aston Villa 128 5.0
MID1 MID Dallas Leeds 171 5.5
MID2 MID Harrison Leeds 160 6.0
MID3 MID Soucek West Ham 147 6.0
MID4 MID Ward-Prowse Southampton 156 6.5
MID5 MID Son Spurs 228 10.0
FWD1 FWD Calvert-Lewin Everton 165 8.0
FWD2 FWD Wood Burnley 138 7.0
FWD3 FWD Kane Spurs 242 12.5

Total Points: 2440
Total Cost: 98.0

GK1 GK Martínez Aston Villa 186 5.5
GK2 GK Meslier Leeds 154 5.0
DEF1 DEF Cresswell West Ham 153 5.5
DEF2 DEF Targett Aston Villa 138 5.0
DEF3 DEF Wan-Bissaka Man Utd 144 5.5
DEF4 DEF Dunk Brighton 130 5.0
DEF5 DEF Mings Aston Villa 128 5.0
MID1 MID Dallas Leeds 171 5.5
MID2 MID Harrison Leeds 160 6.0
MID3 MID Soucek West Ham 147 6.0
MID4 MID Ward-Prowse Southampton 156 6.5
MID5 MID Fernandes Man Utd 244 12.0
FWD1 FWD Calvert-Lewin Everton 165 8.0
FWD2 FWD Wood Burnley 138 7.0
FWD3 FWD Kane Spurs 242 12.5

Total Points: 2456
Total Cost: 100.0

GK1 GK Martínez Aston Villa 186 5.5
GK2 GK Meslier Leeds 154 5.0
DEF1 DEF Cresswell West Ham 153 5.5
DEF2 DEF Targett Aston Villa 138 5.0
DEF3 DEF Wan-Bissaka Man Utd 144 5.5
DEF4 DEF Dunk Brighton 130 5.0
DEF5 DEF Mings Aston Villa 128 5.0
MID1 MID Dallas Leeds 171 5.5
MID2 MID Soucek West Ham 147 6.0
MID3 MID Ward-Prowse Southampton 156 6.5
MID4 MID Son Spurs 228 10.0
MID5 MID Bowen West Ham 141 6.5
FWD1 FWD Bamford Leeds 194 8.0
FWD2 FWD Calvert-Lewin Everton 165 8.0
FWD3 FWD Kane Spurs 242 12.5

Total Points: 2477
Total Cost: 99.5
```

## Searching for better teams

Was able to write a constraint for the previous score that the next selection must improve on.
This works but the search takes a long time and doesn't really improve on what it easily achievable by just looking.

Tried narrowing the pool of players and the order in which different positions were filled. Doesn't really make much difference.