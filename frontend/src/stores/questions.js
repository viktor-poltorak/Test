import { defineStore } from "pinia";
import axios from "axios";

export const useQuestionsStore = defineStore(
  "questions",
  {
    state: () => ({
        questions: []
    }),

    getters: {

    },

    actions: {
        async fetchQuestions() {
            this.questions = await axios.get(`/api/questions/`).then(r => r.data);
        },
        async createQuestion(text) {
            await axios.post(`/api/questions/`, {text: text}).then(r => r.data);
            await this.fetchQuestions()
        },

        async updateQuestion(questionId, text) {
            const item = await axios.put(`/api/questions/${questionId}/`, {text: text}).then(r => r.data);
            await this.fetchQuestions()
        },
        async deleteQuestion(questionId) {
            await axios.delete(`/api/questions/${questionId}/`).then(r => r.data);
            await this.fetchQuestions()
        },
        async createChoice(questionId, text) {
            await axios.post(`/api/choices/`, {
              "question": questionId, text: text
            }).then(r => r.data);
            await this.fetchQuestions()
        },
        async updateChoice(questionId, choiceId, text) {
            await axios.put(`/api/choices/${choiceId}/`, {
              question: questionId,
              text: text
            }).then(r => r.data);
            await this.fetchQuestions()
        },

        async deleteChoice(choiceId) {
            await axios.delete(`/api/choices/${choiceId}/`).then(r => r.data);
            await this.fetchQuestions()
        }
    },
});

