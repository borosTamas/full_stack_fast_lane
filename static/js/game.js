var map = {
    cols: 8,
    rows: 8,
    tsize: 64,
    tiles: [
        1, 3, 3, 3, 1, 1, 3, 1,
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 2, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 2, 1, 1, 1, 1,
        1, 1, 1, 1, 2, 1, 1, 1,
        1, 1, 1, 1, 2, 1, 1, 1,
        1, 1, 1, 0, 0, 1, 1, 1
    ],
    getTile: function (col, row) {
        return this.tiles[row * map.cols + col]
    }
};

for (var c = 0; c < map.cols; c++) {
    for (var r = 0; r < map.rows; r++) {
        var tile = map.getTile(c, r);
    }
}

for(tile of map.tiles){
    if (tile === 1) {
            tile.style.color = "red"
        } else if (tile === 2) {
            tile.style.color = "blue"
        } else if (tile === 3) {
            tile.style.color = "green"
        } else {
            tile.style.color = "black"
        }
}