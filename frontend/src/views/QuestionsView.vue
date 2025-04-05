<script>
import { useQuestionsStore } from "@/stores/questions";

import Questions from "@/components/Questions.vue";

const questionsStore = useQuestionsStore();

export default {
  components: { Questions },
  setup() {

    async function loadQuestions() {
      await questionsStore.fetchQuestions();
    }

    return {
      questionsStore,
      loadQuestions,
    }
  },
  async created() {
      await this.loadQuestions()
  },

}
</script>

<template>
    <div>
      <h1>Questions</h1>
      <Questions :questions="questionsStore.questions"></Questions>
    </div>
</template>

<style>
  .required-field {
    border: 1px solid red;
  }
</style>
