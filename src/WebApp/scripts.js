const limitesAceitaveis = {
    fixedAcidity: { min: 7.1, max: 9.2 },
    volatileAcidity: { min: 0.39, max: 0.64 },
    chlorides: { min: 0.07, max: 0.09 },
    totalSulfurDioxide: { min: 22, max: 62 },
    sulphates: { min: 0.62, max: 0.73 },
    alcohol: { min: 9.5, max: 10.2 }
};

$(document).ready(function() {
    Object.keys(limitesAceitaveis).forEach(campo => {
        $(`#${campo}`).on('input', function() {
            const valor = parseFloat($(this).val());
            const { min, max } = limitesAceitaveis[campo];

            if (valor < min || valor > max) {
                // Mostra o alerta se o valor estiver fora dos limites
                $(`#${campo}Alert`).remove();
                $(this).after(`<p id="${campo}Alert" style="color: red;">Valor fora do limite aceitável de ${min} - ${max}</p>`);
            } else {
                $(`#${campo}Alert`).remove();
            }
        });
    });

    $('#wineQualityForm').on('submit', function(e) {
        e.preventDefault(); // Impede o envio normal do formulário

        // var formData = $(this).serialize(); // Serializa os dados do formulário

        var formData = {
            fixedAcidity: $('#fixedAcidity').val(),
            volatileAcidity: $('#volatileAcidity').val(),
            chlorides: $('#chlorides').val(),
            totalSulfurDioxide: $('#totalSulfurDioxide').val(),
            sulphates: $('#sulphates').val(),
            alcohol: $('#alcohol').val(),
        };

        $.ajax({
            type: "POST",
            url: appConfig.apiUrl, // Substitua com a URL da sua API
            contentType: "application/json",
            data: JSON.stringify(formData),
            success: function(response) {
                $('#wineQualityResult').text('Qualidade do Vinho: ' + response.QualidadeDoVinho)
                .css('display', 'block'); // Torna a div visível
            },
            error: function(xhr, status, error) {
                // Lide com erros aqui
                console.error(error);
            }
        });
    });
});