def jump_range(up_to):
    step = 0
    while step < up_to:
        jump = yield step
        print("jump", jump)
        if jump is None:
            jump = 1
            step += jump
            print("step", step)


if __name__ == '__main__':
    iterator = jump_range(10)
    print(next(iterator))  # 0
    print(iterator.send(4))  # jump 4; step 0
    print(next(iterator))  # jump None; step 1; 1
    print(iterator.send(-1))  # jump -1; 1

