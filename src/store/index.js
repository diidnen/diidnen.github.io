import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    time: 0,
    isRunning: false,
    startTime: null,
    initialTime: 1500,
  },

  mutations: {
    SET_TIME(state, time) {
      state.time = time
    },
    SET_INITIAL_TIME(state, time) {
      state.initialTime = time
      state.time = time
    },
    SET_IS_RUNNING(state, isRunning) {
      state.isRunning = isRunning
    },
    SET_START_TIME(state, startTime) {
      state.startTime = startTime
    },
    SET_CURRENT_TASK(state, taskId) {
      state.currentTaskId = taskId
    },
    RESET_TIMER(state) {
      state.time = 0
      state.isRunning = false
      state.startTime = null
    }
  },

  actions: {
    startTimer({ commit, state }) {
      if (!state.isRunning) {
        commit('SET_IS_RUNNING', true)
        commit('SET_START_TIME', Date.now() - ((state.initialTime - state.time) * 1000))
        
        const updateTimer = () => {
          if (state.isRunning) {
            const currentTime = state.initialTime - Math.floor((Date.now() - state.startTime) / 1000)
            commit('SET_TIME', currentTime >= 0 ? currentTime : 0)
            if (currentTime > 0) {
              requestAnimationFrame(updateTimer)
            } else {
              commit('SET_IS_RUNNING', false)
            }
          }
        }
        requestAnimationFrame(updateTimer)
      }
    },

    stopTimer({ commit }) {
      commit('SET_IS_RUNNING', false)
    },

    resetTimer({ commit }) {
      commit('RESET_TIMER')
    },

    setCurrentTask({ commit }, taskId) {
      commit('SET_CURRENT_TASK', taskId)
    }
  },

  getters: {
    formatTime: state => {
      const hours = Math.floor(state.time / 3600)
      const minutes = Math.floor((state.time % 3600) / 60)
      const seconds = state.time % 60
      return {
        hours,
        minutes,
        seconds,
        formatted: `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`
      }
    }
  },

  plugins: [createPersistedState()]
}) 