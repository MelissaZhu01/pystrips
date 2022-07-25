echo
echo '>> Solving pddl/satellite/problems/pfile01.pddl ...'
python pystrips.py solve pddl/satellite/domain.pddl pddl/satellite/problems/pfile01.pddl --heuristics $1 --weight $2
echo

echo '>> Solving pddl/satellite/problems/pfile02.pddl ...'
python pystrips.py solve pddl/satellite/domain.pddl pddl/satellite/problems/pfile02.pddl --heuristics $1 --weight $2
echo

echo '>> Solving pddl/satellite/problems/pfile03.pddl ...'
python pystrips.py solve pddl/satellite/domain.pddl pddl/satellite/problems/pfile03.pddl --heuristics $1 --weight $2
echo

echo '>> Solving pddl/satellite/problems/pfile04.pddl ...'
python pystrips.py solve pddl/satellite/domain.pddl pddl/satellite/problems/pfile04.pddl --heuristics $1 --weight $2
echo

echo '>> Solving pddl/satellite/problems/pfile05.pddl ...'
python pystrips.py solve pddl/satellite/domain.pddl pddl/satellite/problems/pfile05.pddl --heuristics $1 --weight $2
echo