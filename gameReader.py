
def readCode(code:str) -> tuple:
    code = code.split('/')
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    conv = []
    for move in code:
        if move[0] != 'O' and move[0] != '.':
            conv.append((8 - int(move[1]), alpha.index(move[0]), 8 - int(move[4]), alpha.index(move[3])))
        else:
            if move == 'O-O':  # Kingside
                if code.index(move) % 2 == 0:  # White's Turn
                    conv.append((7, 4, 7, 6))
                    conv.append((0, 0, 0, 0))  # other team does nothing so 2 moves can be done to castle
                    conv.append((7, 7, 7, 5))
                else:  # Black's Turn
                    conv.append((0, 4, 0, 6))
                    conv.append((0, 0, 0, 0))  # other team does nothing again
                    conv.append((0, 7, 0, 5))
                code.insert(code.index('O-O') + 1, '.')
                code.insert(code.index('O-O') + 1, '.')
            elif move == 'O-O-O':  # Queenside
                if code.index(move) % 2 == 0:  # White's Turn:
                    conv.append((7, 4, 7, 2))
                    conv.append((0, 0, 0, 0))  # other team does nothing again
                    conv.append((7, 0, 7, 3))
                else:  # Black's turn
                    conv.append((0, 4, 0, 2))
                    conv.append((0, 0, 0, 0))  # other team does nothing again
                    conv.append((0, 0, 0, 3))
                code.insert(code.index('O-O-O') + 1, '.')
                code.insert(code.index('O-O-O') + 1, '.')
    return conv, code
if __name__ == '__main__':
    codeInput = input("Input code to be read: ")
    print(readCode(codeInput))