# class BoardGame:
#     def __init__(self):
#         self.board = []
#         self.ladders = {4:10, 11:22, 18:29}
#         self.rabbithole = {12:1, 17:12, 28:17}
#         self.players = {1:alice, 2: cat}
#         self.positions = {1:0, 2:0} #player starting positions
#         self.current_player = 1
#         self.x = 65
#         self.y = 510
#         self.m = []
#         self.move = 1
#         self.turn = 0
#         self.player = []
#         self.position = []
#
#
#
#     def pieces(self, move, turn):
#             # Starting value of and x and y should be 120 and 120
#             # In create_circle initial value of x and y should be 100 and 550
#             # To reach to the last block x should be 5*x and y should be 4*y
#             # X should be added to value and Y should be subtracted
#             # 5x120=600 and 4*120=480
#             # m is the constant that tells which side to move i.e. left to right or right to left
#         for i in range(move, 0, -1):
#             self.x = self.x + 120 * self.m[turn]
#
#             if self.x > 665 and turn < 3:
#                 self.y = self.y - 120
#                 self.x = 665
#                 self.m[turn] = -1
#             elif self.x > 700 and turn >= 3:
#                 self.y = self.y - 120
#                 self.x = 700
#                 self.m[turn] = -1
#             if self.x < 65 and turn < 3:
#                 self.x = 65
#                 self.y -= 120
#                 self.m[turn] = 1
#             elif self.x < 100 and turn >= 3:
#                 self.x = 100
#                 self.y -= 120
#                 self.m[turn] = 1
#             if self.y < 30:
#                 self.y = 30
#
#             # Code For the Animation of piece
#             self.canvas.delete(self.player[turn])
#             self.player[turn] = self.canvas.create_circle(self.x, self.y, 15, fill=self.color[turn],
#                                                               outline=self.color[turn])
#             self.canvas.update()
#             time.sleep(0.25)
