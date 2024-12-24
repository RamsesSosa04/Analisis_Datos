document.addEventListener("DOMContentLoaded", function () {
    const leagueDropdown = document.getElementById("leagueDropdown");
    const matchDropdown = document.getElementById("matchDropdown");
    const matchDetails = document.getElementById("matchDetails");

    // Cuando cambia la liga
    leagueDropdown.addEventListener("change", function () {
        const league = leagueDropdown.value;
        matchDropdown.innerHTML = '<option value="">-- Selecciona un partido --</option>';
        matchDropdown.disabled = true;

        if (league) {
            fetch(`/get_matches/${league}`)
                .then(response => response.json())
                .then(matches => {
                    matches.forEach(match => {
                        const option = document.createElement("option");
                        option.value = `${match.Equipo1} vs ${match.Equipo2}`;
                        option.textContent = `${match.Equipo1} vs ${match.Equipo2} (${match.Date})`;
                        matchDropdown.appendChild(option);
                    });
                    matchDropdown.disabled = false;
                });
        }
    });

    // Cuando cambia el partido
    matchDropdown.addEventListener("change", function () {
        const selectedMatch = matchDropdown.value;
        matchDetails.textContent = selectedMatch
            ? `Has seleccionado: ${selectedMatch}`
            : "No se ha seleccionado ningún partido.";
    });
});

