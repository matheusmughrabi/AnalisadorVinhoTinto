class PropriedadesVinho {
    constructor(name, min, max) {
        this.name = name;
        this.min = min;
        this.max = max;
    }

    ehValido(value) {
        return value >= this.min && value <= this.max;
    }

    mostrarAviso(element) {
        if (!this.ehValido(parseFloat(element.val()))) {
            element.siblings(`#${this.name}Alert`).remove();
            element.after(`<p id="${this.name}Alert" style="color: red;">Valor fora do limite aceitável de ${this.min} - ${this.max}</p>`);
        } else {
            element.siblings(`#${this.name}Alert`).remove();
        }
    }
}

class PropriedadesVinhoForm {
    constructor(properties, apiUrl) {
        this.properties = properties;
        this.apiUrl = apiUrl;
        this.formData = {};
    }

    inicializar() {
        Object.values(this.properties).forEach(property => {
            $(`#${property.name}`).on('input', function() {
                property.mostrarAviso($(this));
            });
        });

        $('#wineQualityForm').on('submit', (e) => this.submeter(e));
    }

    submeter(e) {
        e.preventDefault();

        this.formData = Object.fromEntries(Object.values(this.properties).map(property => {
            return [property.name, $(`#${property.name}`).val()];
        }));

        $.ajax({
            type: "POST",
            url: this.apiUrl,
            contentType: "application/json",
            data: JSON.stringify(this.formData),
            success: (response) => this.executarFluxoSucesso(response),
            error: (xhr, status, error) => this.executarFluxoErro(error)
        });
    }

    executarFluxoSucesso(response) {
        $('#wineQualityResult').text('Qualidade do Vinho: ' + response.QualidadeDoVinho)
            .css('display', 'block');
    }

    executarFluxoErro(error) {
        alert('Ocorreu um erro ao submeter formulário.')
    }
}

$(document).ready(function() {
    const properties = {
        fixedAcidity: new PropriedadesVinho('fixedAcidity', 7.1, 9.2),
        volatileAcidity: new PropriedadesVinho('volatileAcidity', 0.39, 0.64),
        chlorides: new PropriedadesVinho('chlorides', 0.07, 0.09),
        totalSulfurDioxide: new PropriedadesVinho('totalSulfurDioxide', 22, 62),
        sulphates: new PropriedadesVinho('sulphates', 0.62, 0.73),
        alcohol: new PropriedadesVinho('alcohol', 9.5, 10.2),
    };

    const apiUrl = appConfig.apiUrl; // Substitua com a URL da sua API
    const wineQualityForm = new PropriedadesVinhoForm(properties, apiUrl);
    wineQualityForm.inicializar();
});
