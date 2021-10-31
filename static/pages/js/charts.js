function totalPopulationPieChart(male = 0, female = 0) {
    new Chart(document.getElementById("pieChartTotalGraduates"), {
        type: 'pie',
        data: {
            labels: ["Male", "Female"],
            datasets: [{
                backgroundColor: ["#2c9be7", "#fa2b79"],
                data: [male, female]
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                },
                title: {
                    display: false,
                    text: 'Total Number of Graduates: '
                }
            }
        }
    });
}

function stackedDoctorateAndDocent(doctorate_male = 0, docent_male = 0, doctorate_female = 0, docent_female = 0) {
    const ctx = document.getElementById('stackedBarChartDoctorateAndDocent').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Doctorate', 'Docent',],
            datasets: [{
                label: 'Male',
                data: [doctorate_male, docent_male,],
                backgroundColor: ["#2c9be7", "#2c9be7"],
            },
                {
                    label: 'Female',
                    data: [doctorate_female, docent_female,],
                    backgroundColor: ["#fa2b79", "#fa2b79"],
                }
            ],
        },
        options: {
            scales: {
                x: {
                    beginsAtZero: true,
                    stacked: true,
                },
                y: {
                    beginsAtZero: true,
                    stacked: true,
                }

            }
        }
    });
}

function barChartPracticeMedicine(avr_male = 0, avr_female = 0) {
    new Chart(document.getElementById("barChartPracticeMedicine"), {
        type: 'bar',
        data: {
            labels: ["Male", "Female"],
            datasets: [
                {
                    backgroundColor: ["#2c9be7", "#fa2b79"],
                    data: [avr_male, avr_female]
                }
            ]
        },
        options: {
            plugins: {
                legend: { display: false },
                title: {
                    display: true,
                    text: 'Avr Practice Medicine in years'
                }
            },
        }
    });
}