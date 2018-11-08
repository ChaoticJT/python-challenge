import CSV
import os

ElectionData = os.path.join("Resources/election_data.csv" )
ElectionsAnalysis = os.path.join("analysis","election_analysis.txt" )

with open(ElectionData) as ElectionData:
    ElectionReader = csv.reader(ElectionData)

    header = next(ElectionReader)

#Parameters
VoteTotal = 0
Candidates = []
CandidateVotes = {}
WinningVote = 0
WinningCandidate = ""

for row in ElectionReader:

    candidateName = row[2]
    VoteTotal = VoteTotal + 1

    if candidateName not in Candidates:
        Candidates.append(candidateName)
        CandidateVotes[candidateName] = 0
    CandidateVotes[candidateName] = CandidateVotes[candidateName] + 1
with open(ElectionsAnalysis, "w") as txt_file:
     ElectionResults = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(ElectionResults, end="")

for candidate in CandidateVotes:
    votes = CandidateVotes.get(candidate)
    votePercent = float(CandidateVotes) / float(VoteTotal)

        if (votes > WinningVote):
            WinningVote = votes
            WinningCandidate = candidate

        CandidateData = f"{candidate}: {votePercent:.3f}% ({votes})\n"
        print(CandidateData, end="")

        txt_file.write(CandidateData)

    WinningTxt = (
        f"-------------------------\n"
        f"Winner: {WinningCandidate}\n"
        f"-------------------------\n")
    print(WinningTxt)

    txt_file.write(WinningTxt)
