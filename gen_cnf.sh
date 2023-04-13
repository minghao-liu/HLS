cats=(1 2 3 4 5 6 7)
amo=$1

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 7 --holes "[[0],[1],[2],[3],[4],[5,6]]" --postfix "1^5_2^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 7 --holes "[[0],[1],[2],[3,4],[5,6]]" --postfix "1^3_2^2" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 7 --holes "[[0],[1,2],[3,4],[5,6]]" --postfix "1^1_2^3" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 8 --holes "[[0],[1],[2],[3],[4],[5],[6,7]]" --postfix "1^6_2^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 8 --holes "[[0],[1],[2],[3],[4,5],[6,7]]" --postfix "1^4_2^2" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 8 --holes "[[0,1],[2,3],[4,5],[6,7]]" --postfix "2^4" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 8 --holes "[[0],[1],[2,3],[4,5],[6,7]]" --postfix "1^2_2^3" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 9 --holes "[[0],[1],[2],[3],[4],[5],[6],[7,8]]" --postfix "1^7_2^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 9 --holes "[[0],[1],[2],[3],[4],[5,6],[7,8]]" --postfix "1^5_2^2" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 9 --holes "[[0],[1],[2],[3,4],[5,6],[7,8]]" --postfix "1^3_2^3" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 9 --holes "[[0],[1,2],[3,4],[5,6],[7,8]]" --postfix "1^1_2^4" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 10 --holes "[[0],[1],[2],[3],[4],[5],[6],[7],[8,9]]" --postfix "1^8_2^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 10 --holes "[[0],[1],[2],[3],[4],[5],[6],[7,8,9]]" --postfix "1^7_3^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 10 --holes "[[0,1],[2,3],[4,5],[6,7],[8,9]]" --postfix "2^5" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 10 --holes "[[0],[1],[2,3],[4,5],[6,7],[8,9]]" --postfix "1^2_2^4" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 10 --holes "[[0],[1],[2],[3],[4,5],[6,7],[8,9]]" --postfix "1^4_2^3" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 11 --holes "[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9,10]]" --postfix "1^9_2^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 11 --holes "[[0],[1],[2],[3],[4],[5],[6],[7],[8,9,10]]" --postfix "1^8_3^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 11 --holes "[[0],[1],[2],[3],[4],[5,6],[7,8],[9,10]]" --postfix "1^5_2^3" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 11 --holes "[[0],[1,2],[3,4],[5,6],[7,8],[9,10]]" --postfix "1^1_2^5" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 11 --holes "[[0,1],[2,3],[4,5],[6,7],[8,9,10]]" --postfix "2^4_3^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 12 --holes "[[0],[1],[2],[3],[4],[5],[6],[7],[8,9],[10,11]]" --postfix "1^8_2^2" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 12 --holes "[[0],[1],[2],[3],[4],[5],[6,7,8],[9,10,11]]" --postfix "1^6_3^2" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 12 --holes "[[0],[1],[2],[3],[4,5],[6,7],[8,9],[10,11]]" --postfix "1^4_2^4" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 12 --holes "[[0,1],[2,3],[4,5],[6,7,8],[9,10,11]]" --postfix "2^3_3^2" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 12 --holes "[[0,1],[2,3],[4,5],[6,7],[8,9],[10,11]]" --postfix "2^6" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 12 --holes "[[0,1,2],[3,4,5],[6,7,8],[9,10,11]]" --postfix "3^4" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 13 --holes "[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9,10,11,12]]" --postfix "1^9_4^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 13 --holes "[[0],[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]" --postfix "1^1_2^6" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 13 --holes "[[0],[1],[2],[3],[4],[5],[6],[7,8,9],[10,11,12]]" --postfix "1^7_3^2" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 13 --holes "[[0],[1,2,3],[4,5,6],[7,8,9],[10,11,12]]" --postfix "1^1_3^4" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 13 --holes "[[0,1],[2,3],[4,5],[6,7],[8,9],[10,11,12]]" --postfix "2^5_3^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 13 --holes "[[0],[1],[2],[3],[4,5],[6,7],[8,9],[10,11,12]]" --postfix "1^4_2^3_3^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 14 --holes "[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12,13]]" --postfix "1^12_2^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 14 --holes "[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11,12,13]]" --postfix "1^11_3^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 14 --holes "[[0,1],[2,3,4],[5,6,7],[8,9,10],[11,12,13]]" --postfix "2^1_3^4" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 14 --holes "[[0,1],[2,3],[4,5],[6,7],[8,9],[10,11,12,13]]" --postfix "2^5_4^1" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 14 --holes "[[0,1],[2,3],[4,5],[6,7],[8,9],[10,11],[12,13]]" --postfix "2^7" --cat $c --amo "$amo"
done

for c in ${cats[@]}
do
  python hls_to_sat.py \
    --order 14 --holes "[[0],[1],[2],[3],[4,5],[6,7],[8,9],[10,11,12,13]]" --postfix "1^4_2^3_4^1" --cat $c --amo "$amo"
done