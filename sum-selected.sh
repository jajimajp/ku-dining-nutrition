cat tmp/基本メニュー栄養.txt| awk '{if ($1~"-.**") {a+=$2;b+=$3}}END{print a, b}' 