document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('portfolioForm');
    const result = document.getElementById('result');
    const portfolioDetails = document.getElementById('portfolioDetails');

    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        const formData = {
            risk_level: form.risk_level.value,
            investment_amount: parseFloat(form.investment_amount.value)
        };

        try {
            const response = await fetch('/get_portfolio', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();
            displayPortfolio(data);
        } catch (error) {
            console.error('Error:', error);
        }
    });

    function formatCurrency(amount) {
        return new Intl.NumberFormat('en-IN', {
            style: 'currency',
            currency: 'INR',
            maximumFractionDigits: 0
        }).format(amount);
    }

    function displayPortfolio(data) {
        result.classList.remove('hidden');

        let html = `
            <div class="bg-blue-50 p-4 rounded mb-6">
                <p class="font-bold text-lg">Risk Profile: ${data.risk_level.charAt(0).toUpperCase() + data.risk_level.slice(1)}</p>
                <p class="font-bold">Total Investment: ${formatCurrency(data.total_amount)}</p>
                <p class="mt-2">Time Horizon: ${data.general_advice.time_horizon}</p>
            </div>
        `;

        // Display allocations
        html += '<div class="space-y-4">';
        for (const [category, details] of Object.entries(data.allocations)) {
            html += `
                <div class="bg-white p-4 rounded shadow border">
                    <h4 class="font-bold text-lg text-blue-600">${category}</h4>
                    <div class="grid grid-cols-2 gap-4 mt-2">
                        <div>
                            <p class="font-semibold">Allocation: ${(details.percentage * 100).toFixed(1)}%</p>
                            <p>Amount: ${formatCurrency(details.amount)}</p>
                            <p>Suggested Monthly SIP: ${formatCurrency(details.monthly_sip)}</p>
                        </div>
                        <div>
                            <p class="font-semibold">Recommended Funds:</p>
                            <ul class="list-disc list-inside">
                                ${details.recommended_funds.map(fund => `<li>${fund}</li>`).join('')}
                            </ul>
                        </div>
                    </div>
                </div>
            `;
        }
        html += '</div>';

        // Display advice
        html += `
            <div class="mt-6 bg-green-50 p-4 rounded">
                <h4 class="font-bold text-lg mb-2">Key Investment Points:</h4>
                <ul class="list-disc list-inside">
                    ${data.general_advice.key_points.map(point => `<li>${point}</li>`).join('')}
                </ul>
            </div>
        `;

        portfolioDetails.innerHTML = html;
    }
});