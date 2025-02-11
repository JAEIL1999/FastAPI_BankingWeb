let currentYear = new Date().getFullYear();
let currentMonth = new Date().getMonth(); // 0~11

const backendUrl = "http://localhost:8000"; // FastAPI 서버 주소

async function fetchTransactions() {
  const userId = "test1"; // 실제 유저 ID로 변경
  try {
    const response = await fetch(`${backendUrl}/users/${userId}/transactions/monthly/${currentYear}/${currentMonth + 1}`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const transactions = await response.json();
    return transactions;
  } catch (error) {
    console.error("Failed to fetch transactions:", error);
    return null;
  }
}


async function generateCalendar() {
  const transactions = await fetchTransactions(); // 거래 내역 가져오기
  const calendarContainer = document.getElementById('calendar');

  const firstDayOfMonth = new Date(currentYear, currentMonth, 1);
  const lastDayOfMonth = new Date(currentYear, currentMonth + 1, 0);
  
  const daysInMonth = lastDayOfMonth.getDate();
  const firstDayOfWeek = firstDayOfMonth.getDay();

  let calendarHTML = `
    <div class="calendar-header">
      <button onclick="changeMonth(-1)">◀</button>
      <span>${currentYear}년 ${currentMonth + 1}월</span>
      <button onclick="changeMonth(1)">▶</button>
    </div>
    <table>
      <tr>
        <th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th>
      </tr>
      <tr>`;

  for (let i = 0; i < firstDayOfWeek; i++) {
    calendarHTML += '<td></td>';
  }

  for (let day = 1; day <= daysInMonth; day++) {
    const transactionData = transactions[day] || { out: 0, in: 0 };
    calendarHTML += `
      <td class="calendar-day">
        <div>${day}</div>
        <div class="transactions">
          <span class="out">-${transactionData.out.toLocaleString()}</span>
          <span class="in">+${transactionData.in.toLocaleString()}</span>
        </div>
      </td>`;

    if ((firstDayOfWeek + day) % 7 === 0) {
      calendarHTML += '</tr><tr>';
    }
  }

  calendarHTML += '</tr></table>';
  calendarContainer.innerHTML = calendarHTML;
}

function changeMonth(offset) {
  currentMonth += offset;
  if (currentMonth < 0) {
    currentMonth = 11;
    currentYear--;
  } else if (currentMonth > 11) {
    currentMonth = 0;
    currentYear++;
  }
  generateCalendar();
}

document.addEventListener('DOMContentLoaded', generateCalendar);






  

  