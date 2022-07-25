echo '>> Solving pddl/satellite/problems/pfile09.pddl ...'
python3 pystrips.py solve pddl/satellite/domain.pddl pddl/satellite/problems/pfile09.pddl --heuristics $1 --weight $2
echo
