

def evaluate(board, color):
    """
    200(K-K') +
    9(Q-Q') +
    5(R-R') +
    3(B-B' + N-N') +
    1(P-P') +
    -0.5(D-D' + S-S' + I-I') +
    0.1(M-M') + ...

    Basically your score minus opponent score
    D, S, I = doubled, blocked, isolated pawns
    """
    pass

"""
alpha = minimum score that the maximizing player is assured
beta = maximum score that the minimizing player is assured
"""

def alpha_beta_max(alpha, beta, depth_left):
    if depth_left == 0:
        return evaluate()
    for {all moves} :
        score = alpha_beta_min(alpha, beta, depth_left-1)
        if score >= beta: # fail hard beta-cutoff
            return beta
        if score > alpha:
            alpha = score # alpha acts like max in minimax
    return alpha

def alpha_beta_min(alpha, beta, depth_left):
    if depth_left == 0:
        return evaluate()
    for all moves:
        score = alpha_beta_max(alpha, beta, depth_left-1)
        if score <= alpha:
            return alpha
        if score < beta:
            beta = score
    return beta
