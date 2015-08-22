function calculateFancyRent() {
    alert("Not yet implemented.");
}

function calculateSimpleRent() {
    function calculatePreferences() {
        return $("#preferences").val();
    }
    function totalRent() {
        return $("input#totalRent").val();
    }
    $.ajax({
        "url": "splitRent",
        "data": {
            "preferences": calculatePreferences(),
            "totalRent": totalRent(),
        },
        "success": function(data, textStatus, jqXHR) {
            data = JSON.parse(data);
            output = "Solution:\n" + data.solution + "\n\nEnvy matrix:\n" + data.envies + "\n\nIs the solution envy-free? " + (data.envyFree? "yes" : "no");
            $("pre#simpleResults").html(output);
            $("pre#simpleResults").css("display", "");
        },
        "error": function(jqXHR, textStatus, errorThrown) {
            alert("Error: " + errorThrown);
        }
    });
}

$(document).ready(function() {
    var numRooms = 0;

    function updateTableSize() {
        var newNumRooms = parseInt($("#numRooms").val());
        if (newNumRooms == NaN) {
            // TODO better error message
            alert("Please enter a number.");
        } else {
            if (numRooms > newNumRooms) {
                var numToRemove = numRooms - newNumRooms;
                for (var i=0; i<numToRemove; i++) {
                    $("#preferencesTable tr:last-child").remove();
                }
                for (var i=0; i<numToRemove; i++) {
                    $("#preferencesTable tr td:last-child").remove();
                }
            } else if (numRooms < newNumRooms) {
                var numToAdd = newNumRooms - numRooms;
                var newColCells = "";
                for(var i=0; i<numRooms; i++) {
                    newColCells += "<td><input></input></td>";
                }
                for(var i=0; i<numToAdd; i++) {
                    $("#preferencesTable").append("<tr class='person'><td><input value='Person 1'></input></td>" + newColCells + "</tr>");
                }
                for(var i=0; i<numToAdd; i++) {
                    $("#preferencesTable tr.header").append("<td><input value='Room 1'></input></td>");
                    $("#preferencesTable tr.person").append("<td><input></input></td>");
                }
            }
            numRooms = newNumRooms;
        }
    };

    updateTableSize(3);
    $("#numRooms").focusout(updateTableSize);
});
