<template>
  <div class="timer-page" :class="{ 'dark-mode': isDarkMode }">
    <div class="timer-grid">
      <!-- 计时器面板 -->
      <div class="timer-panel">
        <h1 class="timer-display">{{ formatTime }}</h1>
        
        <!-- 添加任务输入框 -->
        <div class="task-input-container">
          <input 
            v-model="newTask" 
            type="text" 
            placeholder="添加新任务..."
            @keyup.enter="addTask"
            class="task-input"
          >
          <button @click="addTask" class="add-task-btn">
            <span class="material-symbols-outlined">add</span>
          </button>
        </div>

        <!-- 任务列表 -->
        <ul class="task-list">
          <li v-for="(task, index) in tasks" 
              :key="index"
              class="task-item"
              :class="{ 
                'completed': task.completed,
                'active': currentTaskIndex === index 
              }"
              @click="selectTask(index)">
            <span class="task-content">
              <span class="material-symbols-outlined check-icon"
                    @click.stop="toggleTask(index)">
                {{ task.completed ? 'check_circle' : 'radio_button_unchecked' }}
              </span>
              <div class="task-info">
                <p class="task-text">{{ task.name }}</p>
                <span class="task-time">{{ formatTaskTime(task.focusTime) }}</span>
              </div>
            </span>
            <span class="material-symbols-outlined delete-icon"
                  @click.stop="deleteTask(index)">
              close
            </span>
          </li>
        </ul>
      </div>

      <!-- 控制按钮 -->
      <div class="controls-panel">
        <div class="mode-toggle">
          <button @click="toggleDarkMode" class="mode-btn">
            <span class="material-symbols-outlined">
              {{ isDarkMode ? 'light_mode' : 'dark_mode' }}
            </span>
          </button>
        </div>
        <div class="timer-controls">
          <button class="control-btn" @click="toggleTimer">
            <span class="material-symbols-outlined">
              {{ isRunning ? 'pause' : 'play_arrow' }}
            </span>
          </button>
          <button class="control-btn" @click="resetTimer" :disabled="isRunning">
            <span class="material-symbols-outlined">restart_alt</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lato&family=Open+Sans&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');

.timer-page {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'Open Sans', sans-serif;
  background-color: #ffffff;
  transition: all 0.3s ease;
}

.timer-grid {
  width: 450px;
  background-color: #eeeeee;
  padding: 16px;
  border-radius: 24px;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.timer-panel {
  background-color: #ffffff;
  padding: 24px;
  border-radius: 24px;
  margin-bottom: 16px;
}

.timer-display {
  font-family: 'Lato', sans-serif;
  font-size: 48px;
  line-height: 1;
  color: #464646;
  margin-bottom: 24px;
  text-align: center;
}

/* 任务输入样式 */
.task-input-container {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
}

.task-input {
  flex: 1;
  padding: 12px;
  border: 1px solid #eeeeee;
  border-radius: 12px;
  font-size: 14px;
  background: #f7f7f7;
}

.add-task-btn {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: #464646;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

/* 任务列表样式 */
.task-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.task-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px;
  border-radius: 12px;
  background: #f7f7f7;
  transition: all 0.2s ease;
}

.task-content {
  display: flex;
  align-items: center;
  gap: 8px;
}

.task-text {
  font-size: 14px;
  color: #464646;
}

.check-icon, .delete-icon {
  cursor: pointer;
  font-size: 20px;
  color: #464646;
}

.task-item.completed {
  opacity: 0.5;
}

.task-item.completed .task-text {
  text-decoration: line-through;
}

/* 控制面板样式 */
.controls-panel {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  background: #3b3131;
  border-radius: 24px;
  color: #ffffff;
}

.timer-controls {
  display: flex;
  gap: 12px;
}

.control-btn, .mode-btn {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.control-btn:hover, .mode-btn:hover {
  background: rgba(255, 255, 255, 0.2);
}

/* 深色模式 */
.dark-mode {
  background-color: #ffffff;
}

.dark-mode .timer-grid {
  background-color: #333333;
}

.dark-mode .timer-panel {
  background-color: #464646;
}

.dark-mode .timer-display {
  color: #ffffff;
}

.dark-mode .task-input {
  background: #333333;
  border-color: #555555;
  color: #ffffff;
}

.dark-mode .task-item {
  background: #333333;
}

.dark-mode .task-text {
  color: #ffffff;
}

.dark-mode .check-icon,
.dark-mode .delete-icon {
  color: #ffffff;
}

/* 修改深色模式下的控制面板样式 */
.dark-mode .controls-panel {
  background: #ffffff;
  color: #464646;
}

/* 修改深色模式下控制按钮的样式 */
.dark-mode .control-btn,
.dark-mode .mode-btn {
  background: rgba(70, 70, 70, 0.1);
  color: #464646;
}

.dark-mode .control-btn:hover,
.dark-mode .mode-btn:hover {
  background: rgba(70, 70, 70, 0.2);
}

/* 响应式设计 */
@media (max-width: 480px) {
  .timer-grid {
    width: 100%;
    margin: 16px;
  }

  .timer-display {
    font-size: 36px;
  }
}

.task-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.task-time {
  font-size: 12px;
  color: #666666;
}

.dark-mode .task-time {
  color: #999999;
}

.task-item.active {
  border: 2px solid #464646;
}

.dark-mode .task-item.active {
  border-color: #ffffff;
}
</style>

<script>
export default {
  name: 'FocusTimer',
  data() {
    return {
      time: 0, // 从0开始计时
      isRunning: false,
      timer: null,
      newTask: '',
      tasks: [],
      isDarkMode: false,
      currentTaskIndex: -1 // 当前选中的任务索引
    }
  },
  computed: {
    formatTime() {
      const hours = Math.floor(this.time / 3600)
      const minutes = Math.floor((this.time % 3600) / 60)
      const seconds = this.time % 60
      return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`
    }
  },
  methods: {
    addTask() {
      if (this.newTask.trim()) {
        this.tasks.push({
          name: this.newTask,
          completed: false,
          focusTime: 0 // 为每个任务添加专注时间计数
        })
        this.newTask = ''
      }
    },
    
    selectTask(index) {
      this.currentTaskIndex = index
    },

    toggleTask(index) {
      this.tasks[index].completed = !this.tasks[index].completed
    },

    deleteTask(index) {
      this.tasks.splice(index, 1)
    },

    toggleTimer() {
      if (this.isRunning) {
        // 停止计时
        clearInterval(this.timer)
        // 如果有选中的任务，更新任务的专注时间
        if (this.currentTaskIndex !== -1) {
          this.tasks[this.currentTaskIndex].focusTime = this.time
        }
      } else {
        // 开始新的计时 
            this.timer = setInterval(() => {
          this.time++
        }, 1000)
      }
      this.isRunning = !this.isRunning
    },

    resetTimer() {
      this.time = 0
      clearInterval(this.timer)
      this.isRunning = false
    },

    toggleDarkMode() {
      this.isDarkMode = !this.isDarkMode
    },

    formatTaskTime(seconds) {
        
      const hours = Math.floor(seconds / 3600)
      const minutes = Math.floor((seconds % 3600) / 60)
      return `${hours}h ${minutes}m ${seconds%60}s`
    }
  },
  beforeDestroy() {
    if (this.timer) {
      clearInterval(this.timer)
    }
  }
}
</script> 