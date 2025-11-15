document.addEventListener('DOMContentLoaded', function() {
    // Máscaras para CPF e CEP
    const cpfInput = document.getElementById('cpf_vitima');
    const cepInput = document.getElementById('cep_vitima');

    // Máscara CPF
    cpfInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        value = value.replace(/(\d{3})(\d)/, '$1.$2');
        value = value.replace(/(\d{3})(\d)/, '$1.$2');
        value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
        e.target.value = value;
    });

    // Máscara CEP
    cepInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        value = value.replace(/(\d{5})(\d)/, '$1-$2');
        e.target.value = value;
    });

    // Buscar endereço pelo CEP
    cepInput.addEventListener('blur', function() {
        const cep = this.value.replace(/\D/g, '');
        
        if (cep.length === 8) {
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(response => response.json())
                .then(data => {
                    if (!data.erro) {
                        document.getElementById('enderecorua_vitima').value = data.logradouro || '';
                        document.getElementById('enderecocidade_vitima').value = data.localidade || '';
                        document.getElementById('enderecoestado_vitima').value = data.uf || '';
                    }
                })
                .catch(error => {
                    console.log('Erro ao buscar CEP:', error);
                });
        }
    });

    // Validação do formulário
    const form = document.getElementById('victimForm');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Validações básicas
        const nome = document.getElementById('nome_vitima').value.trim();
        const apelido = document.getElementById('apelido_vitima').value.trim();
        const cpf = document.getElementById('cpf_vitima').value;
        const idade = document.getElementById('idade_vitima').value;
        const cep = document.getElementById('cep_vitima').value;
        const rua = document.getElementById('enderecorua_vitima').value.trim();
        const cidade = document.getElementById('enderecocidade_vitima').value.trim();
        const estado = document.getElementById('enderecoestado_vitima').value;

        // Verificar campos obrigatórios
        if (!nome || !apelido || !cpf || !idade || !cep || !rua || !cidade || !estado) {
            alert('Por favor, preencha todos os campos obrigatórios.');
            return;
        }

        // Validar CPF
        if (!validarCPF(cpf)) {
            alert('Por favor, digite um CPF válido.');
            return;
        }

        // Validar idade
        if (idade < 1 || idade > 120) {
            alert('Por favor, digite uma idade válida.');
            return;
        }

        // Se chegou até aqui, o formulário está válido
        alert('Cadastro realizado com sucesso! Entraremos em contato em breve.');
        
        // Aqui você enviaria os dados para o servidor
        console.log('Dados do formulário:', new FormData(form));
        
        // Redirecionar para página principal
        window.location.href = 'index.html';
    });

    // Função para validar CPF
    function validarCPF(cpf) {
        cpf = cpf.replace(/\D/g, '');
        
        if (cpf.length !== 11) return false;
        
        // Verificar se todos os dígitos são iguais
        if (/^(\d)\1{10}$/.test(cpf)) return false;
        
        // Validar dígitos verificadores
        let soma = 0;
        for (let i = 0; i < 9; i++) {
            soma += parseInt(cpf.charAt(i)) * (10 - i);
        }
        let resto = 11 - (soma % 11);
        let digito1 = resto < 2 ? 0 : resto;
        
        soma = 0;
        for (let i = 0; i < 10; i++) {
            soma += parseInt(cpf.charAt(i)) * (11 - i);
        }
        resto = 11 - (soma % 11);
        let digito2 = resto < 2 ? 0 : resto;
        
        return digito1 === parseInt(cpf.charAt(9)) && digito2 === parseInt(cpf.charAt(10));
    }
});
            // Preparar os dados do formulário
            const dados = {
                cpf: document.getElementById('cpf_vitima').value,
                nome: document.getElementById('nome_vitima').value,
                cep: document.getElementById('cep_vitima').value,
                idade: document.getElementById('idade_vitima').value,
                apelido: document.getElementById('apelido_vitima').value.replace(/\D/g, ''), // Remove pontos e traços
                cidade: document.getElementById('cidade_vitima').value,
                estado: document.getElementById('estado_vitima').value,
                rua: document.getElementById('rua_vitima').value,
                num_endereco: document.getElementById('num_endereco_vitima').value,
                complemento_endereco: document.getElementById('complemento_endereco_vitima').value
            };

            // Enviar para a API
            fetch('http://146.235.62.209:8000/api/vitimas/adicionar/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(dados)
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Erro na resposta da API');
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.success) {
                        alert('Cadastro realizado com sucesso! Entraremos em contato em breve.');
                        console.log('Resposta da API:', data);
                        window.location.href = 'vitimas.html';
                    } else {
                        throw new Error(data.message || 'Erro ao cadastrar');
                    }
                })
                .catch(error => {
                    console.error('Erro:', error);
                    alert('Erro ao enviar cadastro: ' + error.message + '. Tente novamente.');

                    // Remover loading
                    submitBtn.classList.remove('loading');
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = 'Enviar Cadastro';
                });
        