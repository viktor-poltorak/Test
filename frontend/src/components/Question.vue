<script setup>
  import { defineProps, ref } from "vue";
  import { useQuestionsStore } from "@/stores/questions";
  import Choices from "@/components/Choices.vue";

  const questionsStore = useQuestionsStore()

  const showForm = ref(false)
  const questionText = ref("")

  const { question } = defineProps(["question"]);

  function onEdit() {
    questionText.value = question.text;
    showForm.value = true;
  }
  function onSave() {
    questionsStore.updateQuestion(question.id, questionText.value)
    showForm.value = false
  }

  function onDelete() {
    questionsStore.deleteQuestion(question.id)
  }

</script>

<template>
  <div>
    <div v-if="!showForm">
      <div class="text">{{question.text}}</div>
      <button @click="onEdit">Edit</button><button @click="onDelete">Delete</button>
    </div>

    <div v-if="showForm">
        <input class="text" v-model="questionText" v-on:keyup.enter="onSave"/>
        <button @click="onSave">Save</button>
    </div>
  </div>
  <div>
    <Choices :question-id="question.id" :choices="question.choices"></Choices>
  </div>
  <br />
  <div>

  </div>
</template>

<style scoped>
  .text {
    min-width: 300px;
    display: inline-block;
  }
</style>
