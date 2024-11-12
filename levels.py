from cell import Cells
from state import State

class LevelManager:
    def __init__(self):
        self.levels = [
    #1
    [
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}],
    [{'type': 'repel', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
     [
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'repel', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}]
],
#4
 [
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'repel', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#5
 [
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'repel', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#6
 [
    [{'type': 'road', 'is_Solve': True}, {'type': 'block', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'iron', 'is_Solve': True}, {'type': 'block', 'is_Solve': False}, {'type': 'iron', 'is_Solve': True}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'iron', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'repel', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#7
[
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'repel', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#8
 [
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'iron', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'iron', 'is_Solve': False}, {'type': 'repel', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'iron', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'block', 'is_Solve': False}]
],
#9
 [
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'repel', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#10
 [
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'repel', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#11
 [
    [{'type': 'repel', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}]
],
#12
 [
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'attract', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#13
 [
    [{'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'iron', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'attract', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#14
[
    [{'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'attract', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#15
 [
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'attract', 'is_Solve': False}]
],
#16
 [
    [{'type': 'road', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'repel', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'attract', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#17
 [
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': True}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'attract', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'repel', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}]
],
#18
 [
    [{'type': 'attract', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}],
    [{'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'repel', 'is_Solve': False}]
],
#19
 [
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': True}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'attract', 'is_Solve': False}, {'type': 'repel', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#20
 [
    [{'type': 'block', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'repel', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'attract', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#21
 [
    [{'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'repel', 'is_Solve': False}, {'type': 'attract', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#22
 [
    [{'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'iron', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'repel', 'is_Solve': True}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'attract', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#23
 [
    [{'type': 'repel', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'block', 'is_Solve': False}, {'type': 'iron', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'attract', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#24
 [
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}],
    [{'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'attract', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'repel', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#25
 [
    [{'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'repel', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}],
    [{'type': 'attract', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}],
    [{'type': 'block', 'is_Solve': False}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
#26
 [
    [{'type': 'iron', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'attract', 'is_Solve': True}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}],
    [{'type': 'repel', 'is_Solve': True}, {'type': 'road', 'is_Solve': True}, {'type': 'road', 'is_Solve': True}, {'type': 'iron', 'is_Solve': False}, {'type': 'block', 'is_Solve': False}]
],
[
     [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False},],
    [{'type': 'road', 'is_Solve': True}, {'type': 'attract', 'is_Solve': False}, ],
],
[
    [{'type': 'road', 'is_Solve': False}, {'type': 'road', 'is_Solve': False},{'type': 'attract', 'is_Solve': False}],
    [{'type': 'iron', 'is_Solve': False}, {'type': 'road', 'is_Solve': False},{'type': 'road', 'is_Solve': True} ]
]
]
    def create_level(self, init_board):
        rows = len(init_board)
        cols = len(init_board[0])
        board = [[None for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                cell_data = init_board[i][j]
                board[i][j] = Cells(i, j, cell_data['type'], cell_data['is_Solve'])
        return State(rows, cols, board)

    def choose_level(self):
        print("Choose level:")
        for index, level in enumerate(self.levels):
            print(f"{index + 1}: Level {index + 1}")

        level_choice = int(input("Enter the number of the level: ")) - 1
        if level_choice < 0 or level_choice >= len(self.levels):
            print("Invalid number, automatically selecting level 1.")
            level_choice = 0

        return self.create_level(self.levels[level_choice])

