function validatePswd() {
    var password = document.getElementById("pass").value;
    var password_repeat = document.getElementById("pass-repeat").value;

    if (password != password_repeat) {
        alert("The first password does not match the second");
        return false;
    }
        alert("Good match!")
    return true;
}

// add event listener to compare the two password
// document.getElementById("comparePassword").addEventListener('click', validatePswd);


var tableData = [];
function createTable() {
    var table = document.getElementById("myTable");
    var columnsInput = document.getElementById("columns");
    var rowsInput = document.getElementById("rows");
    var columns = parseInt(columnsInput.value);
    var rows = parseInt(rowsInput.value);

    // clear existing table
    while (table.firstChild) {
        table.removeChild(table.firstChild);
    }

    // create table header
    var headerRow = document.createElement("tr");
    for (var i=0; i < rows; i++) {
        var rowData = [];
        var row = document.createElement("tr");
        for (var j=0; j < columns; j++) {
            var cell = document.createElement("td");
            cell.setAttribute("contenteditable", "true");
            cell.setAttribute("class", "editable-cell");
            cell.addEventListener("input", updateCell);
            rowData.push("");
            row.appendChild(cell);
        }
        table.appendChild(row);
        tableData.push(rowData)
    }
}

function updateCell(event) {
    var rowIndex = event.target.parentNode.rowIndex - 1;
    var columnIndex = event.target.cellIndex;
    var value = event.target.textContent.trim();
    updateData(rowIndex, columnIndex, value);
}

function updateData(row, col, value) {
    tableData[row][col] = value;
}

function deleteRow(row) {
    var table = document.getElementById("myTable");
    table.deleteRow(row);
    tableData.splice(row, 1);
}

function updateRow(row) {
    var table = document.getElementById("myTable");
    var rowData = table[row];
    var cells = table.rows[row + 1].cells;
    for (var i=0; i < rowData.length; i++) {
        var value = cells[i].textContent.trim();
        rowData[i] = value;
    }
}

function displayData() {
    console.log(tableData);
}

