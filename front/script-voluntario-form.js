document.addEventListener('DOMContentLoaded', function () {
    const cpfInput = document.getElementById('cpf_voluntario');
    const rgInput = document.getElementById('rg_voluntario');
    const telefoneInput = document.getElementById('telefone_voluntario');
    const oabInput = document.getElementById('oab_voluntarioadvogado');


    if (cpfInput) {
        cpfInput.addEventListener('input', function (e) {
            let value = e.target.value.replace(/\D/g, '');
            value = value.replace(/(\d{3})(\d)/, '$1.$2');
            value = value.replace(/(\d{3})(\d)/, '$1.$2');
            value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
            e.target.value = value;
        });
    }

    if (rgInput) {
        rgInput.addEventListener('input', function (e) {
            let value = e.target.value.replace(/\D/g, '');
            e.target.value = value;
        });
    }


    if (telefoneInput) {
        telefoneInput.addEventListener('input', function (e) {
            let value = e.target.value.replace(/\D/g, '');
            e.target.value = value;
        });
    }


    if (oabInput) {
        oabInput.addEventListener('input', function (e) {
            let value = e.target.value.toUpperCase();
            value = value.replace(/[^A-Z0-9]/g, '');
            if (value.length > 2) {
                value = value.substring(0, 2) + '/' + value.substring(2, 8);
            }
            e.target.value = value;
        });
    }

    const dataNascInput = document.getElementById('datanasc_voluntario');
    if (dataNascInput) {
        dataNascInput.addEventListener('change', function () {
            const hoje = new Date();
            const nascimento = new Date(this.value);
            const idade = hoje.getFullYear() - nascimento.getFullYear();
            const mesAtual = hoje.getMonth();
            const mesNascimento = nascimento.getMonth();

            let idadeReal = idade;
            if (mesAtual < mesNascimento || (mesAtual === mesNascimento && hoje.getDate() < nascimento.getDate())) {
                idadeReal--;
            }

            if (idadeReal < 18) {
                this.setCustomValidity('Você deve ter pelo menos 18 anos para se voluntariar.');
                showError(this, 'Você deve ter pelo menos 18 anos para se voluntariar.');
            } else {
                this.setCustomValidity('');
                clearError(this);
            }
        });
    }

    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(input => {
        input.addEventListener('change', function () {
            const file = this.files[0];
            if (file) {

                if (file.size > 5 * 1024 * 1024) {
                    showError(this, 'Arquivo muito grande. Máximo 5MB.');
                    this.value = '';
                    return;
                }


                const allowedTypes = this.accept.split(',').map(type => type.trim());
                const fileExtension = '.' + file.name.split('.').pop().toLowerCase();

                if (!allowedTypes.includes(fileExtension)) {
                    showError(this, 'Tipo de arquivo não permitido.');
                    this.value = '';
                    return;
                }

                clearError(this);
                showFileStatus(this, 'Arquivo selecionado: ' + file.name, 'success');
            }
        });
    });


    const form = document.getElementById('volunteerForm');

    form.addEventListener('submit', function (e) {
        e.preventDefault();


        clearAllErrors();

        let isValid = true;


        const requiredFields = form.querySelectorAll('[required]');
        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                showError(field, 'Este campo é obrigatório.');
                isValid = false;
            }
        });

        if (cpfInput && !validarCPF(cpfInput.value)) {
            showError(cpfInput, 'CPF inválido.');
            isValid = false;
        }

        if (rgInput && rgInput.value.length !== 9) {
            showError(rgInput, 'RG deve ter 9 dígitos.');
            isValid = false;
        }

        if (telefoneInput && telefoneInput.value.length !== 9) {
            showError(telefoneInput, 'Telefone deve ter 9 dígitos.');
            isValid = false;
        }

        if (oabInput && !validarOAB(oabInput.value)) {
            showError(oabInput, 'Formato de OAB inválido. Use: UF/123456');
            isValid = false;
        }

        fileInputs.forEach(input => {
            if (input.hasAttribute('required') && !input.files[0]) {
                showError(input, 'Este documento é obrigatório.');
                isValid = false;
            }
        });

        if (isValid) {
            const submitBtn = form.querySelector('.submit-btn');
            submitBtn.classList.add('loading');
            submitBtn.disabled = true;
            submitBtn.innerHTML = 'Enviando... <span class="loading-spinner"></span>';


            const dados = {
                nome: document.getElementById('nomecompleto_voluntario').value,
                email: document.getElementById('email_voluntario').value,
                dataNascimento: document.getElementById('datanasc_voluntario').value,
                sexo: document.getElementById('sexo_voluntario').value,
                cpf: document.getElementById('cpf_voluntario').value.replace(/\D/g, ''), // Remove pontos e traços
                rg: document.getElementById('rg_voluntario').value,
                telefone: document.getElementById('telefone_voluntario').value,
                instagram: document.getElementById('instagram_voluntario').value,
                endereco: document.getElementById('enderecorua_voluntario').value,
                cidade: document.getElementById('enderecocidade_voluntario').value,
                estado: document.getElementById('enderecoestado_voluntario').value || '',
                cpfupload: true,
                fotoupload: true,
                termoupload: true
            };

            try {
                DadoOAB = document.getElementById('oab_voluntarioadvogado').value
                dados["oab"] = DadoOAB
            } catch (e) {
                console.log("ERRO:", e)
            }

            try {
                DADOScursoBacharel = document.getElementById('cursoformacao_voluntariobacharel').value
                dados["cursoBacharel"] = DADOScursoBacharel
            } catch (e) {
                console.log("ERRO:", e)
            }

            try {
                DADOSCurso = document.getElementById('cursonome_voluntarioestagiario').value
                DADOSPeriodo = document.getElementById('cursoperido_voluntarioestagiario').value
                dados["curso"] = DADOSCurso
                dados["periodo"] = DADOSPeriodo
            } catch (e) {
                console.log("ERRO:", e)
            }

            URL_Base = 'http://146.235.62.209:8000/'
            Rota = ''

            if (dados.oab) {
                Rota = 'api/voluntarios/adicionar/advogado/'
            } else if (dados.cursoBacharel) {
                Rota = 'api/voluntarios/adicionar/bacharel/'
            } else {
                Rota = 'api/voluntarios/adicionar/estagiario/'
            }

            fetch(`${URL_Base}${Rota}`, {
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
                        window.location.href = 'voluntarios.html';
                    } else {
                        throw new Error(data.message || 'Erro ao cadastrar');
                    }
                })
                .catch(error => {
                    console.error('Erro:', error);
                    alert('Erro ao enviar cadastro: ' + error.message + '. Tente novamente.');


                    submitBtn.classList.remove('loading');
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = 'Enviar Cadastro';
                });
        } else {

            const firstError = form.querySelector('.form-group.error');
            if (firstError) {
                firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }

    });


    function showError(field, message) {
        const formGroup = field.closest('.form-group');
        formGroup.classList.add('error');

        let errorElement = formGroup.querySelector('.error-message');
        if (!errorElement) {
            errorElement = document.createElement('div');
            errorElement.className = 'error-message';
            formGroup.appendChild(errorElement);
        }
        errorElement.textContent = message;
    }

    function clearError(field) {
        const formGroup = field.closest('.form-group');
        formGroup.classList.remove('error');
        const errorElement = formGroup.querySelector('.error-message');
        if (errorElement) {
            errorElement.remove();
        }
    }

    function clearAllErrors() {
        const errorGroups = form.querySelectorAll('.form-group.error');
        errorGroups.forEach(group => {
            group.classList.remove('error');
            const errorElement = group.querySelector('.error-message');
            if (errorElement) {
                errorElement.remove();
            }
        });
    }

    function showFileStatus(field, message, type) {
        const formGroup = field.closest('.form-group');

        let statusElement = formGroup.querySelector('.file-status');
        if (!statusElement) {
            statusElement = document.createElement('div');
            statusElement.className = 'file-status';
            formGroup.appendChild(statusElement);
        }

        statusElement.className = `file-status ${type}`;
        statusElement.innerHTML = `
            <span class="icon">${type === 'success' ? '✓' : '✗'}</span>
            <span>${message}</span>
        `;
    }

    function validarCPF(cpf) {
        cpf = cpf.replace(/\D/g, '');

        if (cpf.length !== 11) return false;
        if (/^(\d)\1{10}$/.test(cpf)) return false;

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

    function validarOAB(oab) {
        const regex = /^[A-Z]{2}\/[0-9]{6}$/;
        return regex.test(oab);
    }


    const formElements = document.querySelectorAll('.form-group');
    formElements.forEach((element, index) => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity 0.5s ease, transform 0.5s ease';

        setTimeout(() => {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }, index * 50);
    });
});