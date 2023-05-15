const timer = document.getElementById("timer");
const startButton = document.getElementById("start");
const pauseButton = document.getElementById("pause");
const resetButton = document.getElementById("reset");
const shortBreakButton = document.getElementById("short-break");
const longBreakButton = document.getElementById("long-break");

let workTime = 25;
let shortBreakTime = 5;
let longBreakTime = 15;
let timeLeft = workTime * 60;
let timerInterval;
let timerRunning = false;
let rest=true
let tasks=[]

function formatTime(timeInSeconds) {
	let minutes = Math.floor(timeInSeconds / 60);
	let seconds = timeInSeconds % 60;
	return `${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
}

function updateTimer() {
	timer.textContent = formatTime(timeLeft);
	}
function startTimer() {
    console.log("startTimer")
	timerRunning = true;
	timerInterval = setInterval(() => {
	timeLeft--;
    if (timeLeft <= 0) {
        resetTimer();
        if (rest==false){
            repDone();
            refreshTasks()
            rest=true
        }
        return
		}
		updateTimer();
	}, 1000);
}

function pauseTimer() {
    console.log("pauseTimer")
	timerRunning = false;
	clearInterval(timerInterval);
}

function resetTimer() {
    console.log("resetTimer")
	pauseTimer();
	timeLeft = workTime * 60;
	updateTimer();
}

function setTimer(duration) {
    console.log("setTimer")
	timeLeft = duration * 60;
    updateTimer();
    resetButton.disabled = false;
    shortBreakButton.disabled = true;
    longBreakButton.disabled = true;
    startTimer();
}
startButton.addEventListener("click", () => {
    rest=false
	if (!timerRunning) {
		startTimer();
	}
});

pauseButton.addEventListener("click", () => {
    if (timerRunning) {
        pauseTimer();
        }
});
resetButton.addEventListener("click", () => {
    if (timerRunning) {
        pauseTimer();
        }
    resetTimer();
        shortBreakButton.disabled = false;
        longBreakButton.disabled = false;
});

shortBreakButton.addEventListener("click", () => {
    rest=true
    if (timerRunning) {
        pauseTimer();
        }
    setTimer(shortBreakTime);
});

longBreakButton.addEventListener("click", () => {
    rest=true
    if (timerRunning) {
        pauseTimer();
        }
    setTimer(longBreakTime);
});

var times=0

function refreshTasks(){
    console.log("refreshTasks")
    console.log(tasks)
    var list = document.getElementById("to-do")
    list.innerHTML=""
    tasks.forEach(task => {
        var listElement=document.createElement("li")
        console.log(task)
        listElement.innerHTML=task.name+" ("+task.done+ "/"+task.reps+")"
        list.append(listElement)


    });
}


function addTask(){
    console.log("addTask")
    var task={}
    var list = document.getElementById("to-do")
    var input = document.getElementById("text").value
    var number = document.getElementById("number").value
    var listElement=document.createElement("li")
    task={name:input,reps:parseInt(number),done:0}
    tasks.push(task)
    refreshTasks()
    

}
function clearTask(){
    console.log("clearTask")
    var list = document.getElementById("to-do")
    list.innerHTML=""
    tasks=[]
}
function startTask(){
    console.log("startTask")
    rest=false
    if (timerRunning) {
        pauseTimer();
        }
    resetTimer();
        shortBreakButton.disabled = false;
        longBreakButton.disabled = false;
    startTimer()
    if (timeLeft <= 0) {
		resetTimer();
        if (rest==false){
            repDone();
            refreshTasks()
            rest=true
        }

		}
}

function repDone(){
    console.log("repDone")
    for (let i=0;i<tasks.length;i++){
        if (tasks[i].done==tasks[i].reps){
            continue
        }
        else{
            tasks[i].done+=1
            break
        }
    }
}