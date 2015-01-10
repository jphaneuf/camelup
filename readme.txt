A script for calculating probability of winning for each camel in the hit board game "camel up."

Currently only set up to compute probability for one round of betting, not for final winner/loser.

Commands are for board setup, placing/removing the forward/backward modifier tokens, removing camel dice from the pyramid (after they've already rolled).

for board setup, use command "board" followed by the relative positions of the camels (bottom camels listed first). First letter of color can be used instead of typing out the whole color.  Example:

####Blue############Green
####White###Orange##Yellow##+1#############-1
commands:
>>>:board w 1 o 2 y 3 b 1 g 3
>>>:forward 4
>>>:back 6
>>>:run

Output is probability of obtaining first, second, third, fourth and fifth place, for each camel.

If some camels have already rolled in a round, you can update the remaining dice.  For instance, if the the blue camel has rolled and the rest are still remaining:
>>>:remaining o g w y

