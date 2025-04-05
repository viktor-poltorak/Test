<script setup>
  import { defineProps, ref } from "vue";
  import { useQuestionsStore } from "@/stores/questions";
  import Question from "@/components/Question.vue";

  const questionsStore = useQuestionsStore()


  const newQuestionText = ref("")
  const showForm = ref(false)
  const { questions } = defineProps(['questions'])

  function createQuestion() {
    if (!newQuestionText.value.toString().trim()) {
      return
    }
    questionsStore.createQuestion(newQuestionText.value)
    newQuestionText.value = "";
    showForm.value = false;
  }

</script>

<template>
  <div>
    <Question v-for="item in questions" :question="item"></Question>
    <br />
    <div v-if="showForm">
      <input class="text" v-model="newQuestionText" />
      <button @click="createQuestion">Save</button>
    </div>
    <div>
      <button @click="showForm=true">Add question</button>
    </div>
  </div>
</template>

<style scoped>
  .text {
    min-width: 300px;
    display: inline-block;
  }
</style>
