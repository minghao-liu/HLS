cats=(1 2 3 4 5 6 7)

for c in ${cats[@]}
do
 python hls_to_smt2.py \
   7 $c "[[0],[1],[2],[3],[4],[5,6]]" "1^5_2^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    7 $c "[[0],[1],[2],[3,4],[5,6]]" "1^3_2^2"
done

 for c in ${cats[@]}
 do
   python hls_to_smt2.py \
     7 $c "[[0],[1,2],[3,4],[5,6]]" "1^1_2^3"
 done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    8 $c "[[0],[1],[2],[3],[4],[5],[6,7]]" "1^6_2^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    8 $c "[[0],[1],[2],[3],[4,5],[6,7]]" "1^4_2^2"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    8 $c "[[0],[1],[2,3],[4,5],[6,7]]" "1^2_2^3"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    8 $c "[[0,1],[2,3],[4,5],[6,7]]" "2^4"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    9 $c "[[0],[1],[2],[3],[4],[5],[6],[7,8]]" "1^7_2^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    9 $c "[[0],[1],[2],[3],[4],[5,6],[7,8]]" "1^5_2^2"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    9 $c "[[0],[1],[2],[3,4],[5,6],[7,8]]" "1^3_2^3"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    9 $c "[[0],[1,2],[3,4],[5,6],[7,8]]" "1^1_2^4"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    10 $c "[[0],[1],[2],[3],[4],[5],[6],[7],[8,9]]" "1^8_2^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    10 $c "[[0],[1],[2],[3],[4],[5],[6],[7,8,9]]" "1^7_3^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    10 $c "[[0,1],[2,3],[4,5],[6,7],[8,9]]" "2^5"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    10 $c "[[0],[1],[2,3],[4,5],[6,7],[8,9]]" "1^2_2^4"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    10 $c "[[0],[1],[2],[3],[4,5],[6,7],[8,9]]" "1^4_2^3"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    11 $c "[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9,10]]" "1^9_2^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    11 $c "[[0],[1],[2],[3],[4],[5],[6],[7],[8,9,10]]" "1^8_3^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    11 $c "[[0],[1],[2],[3],[4],[5,6],[7,8],[9,10]]" "1^5_2^3"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    11 $c "[[0],[1,2],[3,4],[5,6],[7,8],[9,10]]" "1^1_2^5"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    11 $c "[[0,1],[2,3],[4,5],[6,7],[8,9,10]]" "2^4_3^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    12 $c "[[0],[1],[2],[3],[4],[5],[6],[7],[8,9],[10,11]]" "1^8_2^2"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    12 $c "[[0],[1],[2],[3],[4],[5],[6,7,8],[9,10,11]]" "1^6_3^2"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    12 $c "[[0],[1],[2],[3],[4,5],[6,7],[8,9],[10,11]]" "1^4_2^4"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    12 $c "[[0,1],[2,3],[4,5],[6,7,8],[9,10,11]]" "2^3_3^2"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    12 $c "[[0,1],[2,3],[4,5],[6,7],[8,9],[10,11]]" "2^6"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    12 $c "[[0,1,2],[3,4,5],[6,7,8],[9,10,11]]" "3^4"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
     13 $c "[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9,10,11,12]]" "1^9_4^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    13 $c "[[0],[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]" "1^1_2^6"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    13 $c "[[0],[1],[2],[3],[4],[5],[6],[7,8,9],[10,11,12]]" "1^7_3^2"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    13 $c "[[0],[1,2,3],[4,5,6],[7,8,9],[10,11,12]]" "1^1_3^4"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    13 $c "[[0,1],[2,3],[4,5],[6,7],[8,9],[10,11,12]]" "2^5_3^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    13 $c "[[0],[1],[2],[3],[4,5],[6,7],[8,9],[10,11,12]]" "1^4_2^3_3^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    14 $c "[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12,13]]" "1^12_2^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    14 $c "[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11,12,13]]" "1^11_3^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    14 $c "[[0,1],[2,3,4],[5,6,7],[8,9,10],[11,12,13]]" "2^1_3^4"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    14 $c "[[0,1],[2,3],[4,5],[6,7],[8,9],[10,11,12,13]]" "2^5_4^1"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    14 $c "[[0,1],[2,3],[4,5],[6,7],[8,9],[10,11],[12,13]]" "2^7"
done

for c in ${cats[@]}
do
  python hls_to_smt2.py \
    14 $c "[[0],[1],[2],[3],[4,5],[6,7],[8,9],[10,11,12,13]]" "1^4_2^3_4^1"
done
