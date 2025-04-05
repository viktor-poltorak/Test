<script setup>
import { defineProps, ref } from "vue";
import { useQuestionsStore } from "@/stores/questions";

const questionsStore = useQuestionsStore()

const showForm = ref(false)
const text = ref("")

const { questionId, choice } = defineProps(["questionId", "choice"]);

function onEdit() {
  text.value = choice.text;
  showForm.value = true;
}

function onSave() {
  questionsStore.updateChoice(questionId, choice.id, text.value)
  showForm.value = false
}

function onDelete() {
  questionsStore.deleteChoice(choice.id)
}
</script>

<template>
<div>
    <div v-if="!showForm">
      <div class="text">{{choice.text}}</div>
      <button @click="onEdit">Edit</button><button @click="onDelete">Delete</button>
    </div>

    <div v-if="showForm">
        <input class="text" v-model="text" v-on:keyup.enter="onSave"/>
        <button @click="onSave">Save</button>
    </div>
  </div>
</template>

<style scoped>
.text {
  min-width: 280px;
  display: inline-block;
  margin-left: 20px;
}
</style>
