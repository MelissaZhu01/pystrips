echo '>> Solving pddl/satellite/problems/pfile06.pddl ...'
python3 pystrips.py solve pddl/satellite/domain.pddl pddl/satellite/problems/pfile06.pddl --heuristics $1 --weight $2
echo

echo '>> Solving pddl/satellite/problems/pfile07.pddl ...'
python3 pystrips.py solve pddl/satellite/domain.pddl pddl/satellite/problems/pfile07.pddl --heuristics $1 --weight $2
echo

echo '>> Solving pddl/satellite/problems/pfile08.pddl ...'
python3 pystrips.py solve pddl/satellite/domain.pddl pddl/satellite/problems/pfile08.pddl --heuristics $1 --weight $2
echo

echo '>> Solving pddl/satellite/problems/pfile10.pddl ...'
python3 pystrips.py solve pddl/satellite/domain.pddl pddl/satellite/problems/pfile10.pddl --heuristics $1 --weight $2
echo

echo '>> Solving pddl/satellite/problems/pfile09.pddl ...'
python3 pystrips.py solve pddl/satellite/domain.pddl pddl/satellite/problems/pfile09.pddl --heuristics $1 --weight $2
echo
