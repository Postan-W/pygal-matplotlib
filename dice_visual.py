from dice import Dice
import pygal
dice = Dice()

result = []
frequency = []
for roll in range(1000):
    result.append(dice.roll())
for value in range(1,dice.sides + 1):
    frequency.append(result.count(value))

hist = pygal.Bar()
hist._title = "滚动骰子1000次的结果"
hist.x_labels  = ['1','2','3','4','5','6']
hist._x_title = "结果"
hist._y_title = "结果的频率"
hist.add("6面骰子",frequency)
hist.render_to_file('dice_visual.svg')