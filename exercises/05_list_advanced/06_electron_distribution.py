electrons = int(input())
shell = []
iterations = 0

while electrons > 0:
    iterations += 1  # keep track of shell number
    current_electrons = 2 * iterations ** 2  # calculate how many electron should shell has

    # Case when current electrons are less than total electrons
    if electrons > current_electrons:
        shell.append(current_electrons)  # add new shell
        electrons -= current_electrons  # reduce number of electrons

    # Case for last shelf when total electrons are not enough to fill current shell
    else:
        shell.append(electrons)
        electrons = 0

print(shell)
