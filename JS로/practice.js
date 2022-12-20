function sol(s, e) {
    function bfs() {
        let q = [s];
        let visited = [s];
        let level = 1;

        while (q.length) {
            level++;
            for (let _ of q) {
                let curr = q.shift();
                if (curr === e) return level;

                for (let next of [curr - 1, curr + 1, curr + 5]) {
                    if (visited.indexOf(next) === -1) {
                        visited.push(next);
                        q.push(next);
                    }
                }
            }
        }
        return -1;
    }
    return bfs();
}

console.log(sol(8, 3));
console.log(sol(5, 14));
