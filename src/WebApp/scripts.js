$(document).ready(function() {
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