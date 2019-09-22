import pandas as pd


def score(db, email):
    # Read in scoresheet from file
    scoresheetPath = Path('data' / 'solutions.csv')
    scoresheet = pd.read_csv(str(scoresheetPath))

    questions = np.unique(scoresheet['Question #'])

    score = 0

    for i in db.index:
        if db.at[i, "Answer"] == scoresheet.at[i, "Correct Answer"]:
            score += 1

    # Read in database
    dataPath = Path('data' / 'data.csv')
    data = pd.read_csv(str(dataPath))

    # Update score field in db
    data.loc[data["username"] == email, 'score'] = score

    data.to_csv(str(dataPath))

    return score
