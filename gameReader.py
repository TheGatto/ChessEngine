def readCode(code:str) -> tuple:
    code = code.split('/')
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    conv = []
    for move in code:
        if move[0] != 'O':
            if move[2] == '-':
                conv.append([8 - int(move[1]), alpha.index(move[0]), 8 - int(move[4]), alpha.index(move[3]), 0])
            elif move[2] == 'x':
                conv.append([8 - int(move[1]), alpha.index(move[0]), 8 - int(move[4]), alpha.index(move[3]), 'x'])
        else:
            if move == 'O-O':  # Kingside
                if code.index(move) % 2 == 0:  # White's Turn
                    conv.append([0, 0])
                else:  # Black's Turn
                    conv.append([1, 0])
            elif move == 'O-O-O':  # Queenside
                if code.index(move) % 2 == 0:  # White's Turn:
                    conv.append([0, 1])
                else:  # Black's turn
                    conv.append([1, 1])
    return conv
if __name__ == '__main__':
    codeInput = input("Input code to be read: ")
    print(readCode(codeInput))
