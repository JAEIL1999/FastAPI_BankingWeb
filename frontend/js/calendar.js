let currentYear = new Date().getFullYear();
let currentMonth = new Date().getMonth(); // 0-11 (0 = 1월, 11 = 12월)

function generateCalendar() {
  const calendarContainer = document.getElementById('calendar');
  
  // 첫 번째 날짜와 마지막 날짜 계산
  const firstDayOfMonth = new Date(currentYear, currentMonth, 1);
  const lastDayOfMonth = new Date(currentYear, currentMonth + 1, 0);
  
  const daysInMonth = lastDayOfMonth.getDate();
  const firstDayOfWeek = firstDayOfMonth.getDay(); // 일요일 = 0, 월요일 = 1, ...

  // 달력 테이블 구조 생성
  let calendarHTML = `
    <div class="calendar-header">
      <button onclick="changeMonth(-1)">◀</button>
      <span>${currentYear}년 ${currentMonth + 1}월</span>
      <button onclick="changeMonth(1)">▶</button>
    </div>
    <table>
      <tr>
        <th>Sun</th>
        <th>Mon</th>
        <th>Tue</th>
        <th>Wed</th>
        <th>Thu</th>
        <th>Fri</th>
        <th>Sat</th>
      </tr>
      <tr>`;

  // 첫 번째 날 이전에 빈 셀 추가
  for (let i = 0; i < firstDayOfWeek; i++) {
    calendarHTML += '<td></td>';
  }

  // 달력 날짜 추가
  for (let day = 1; day <= daysInMonth; day++) {
    if ((firstDayOfWeek + day - 1) % 7 === 0 && day !== 1) {
      calendarHTML += '</tr><tr>'; // 새로운 주의 시작
    }
    calendarHTML += `<td class="calendar-day" onclick="showTransactions(${day})">${day}</td>`;
  }

  calendarHTML += '</tr></table>';
  calendarContainer.innerHTML = calendarHTML;
}

// 월을 변경하는 함수 (이전/다음)
function changeMonth(offset) {
  currentMonth += offset;

  // 월이 0보다 작으면 12로 설정하고, 연도를 한 년도 빼준다
  if (currentMonth < 0) {
    currentMonth = 11;
    currentYear--;
  }

  // 월이 12 이상이면 0으로 설정하고, 연도를 한 년도 더해준다
  if (currentMonth > 11) {
    currentMonth = 0;
    currentYear++;
  }

  generateCalendar();
}

// 거래 내역을 보여주는 함수
function showTransactions(day) {
  // 해당 날짜 아래에 거래 내역을 표시
  const calendarContainer = document.getElementById('calendar');
  let transactionContainer = document.getElementById(`transactions-${day}`);

  // 만약 거래 내역이 이미 있는 경우, 그 내역을 숨기고 다시 표시하는 방식
  if (!transactionContainer) {
    // 거래 내역을 나타낼 div 생성
    transactionContainer = document.createElement('div');
    transactionContainer.id = `transactions-${day}`;
    transactionContainer.classList.add('transactions');
    transactionContainer.innerHTML = `
      <h4>${currentYear}년 ${currentMonth + 1}월 ${day}일의 거래 내역</h4>
      <p>거래 내역이 여기에 표시됩니다.</p>
    `;

    // 클릭한 날짜 아래에 거래 내역을 추가
    const calendarDays = document.querySelectorAll('.calendar-day');
    calendarDays.forEach((td) => {
      if (td.textContent == day) {
        td.appendChild(transactionContainer);
      }
    });
  } else {
    // 이미 거래 내역이 표시되어 있다면, 숨기거나 다시 표시
    transactionContainer.style.display = transactionContainer.style.display === 'none' ? 'block' : 'none';
  }
}

// 페이지가 로드된 후 달력 생성
document.addEventListener('DOMContentLoaded', generateCalendar);


  

  