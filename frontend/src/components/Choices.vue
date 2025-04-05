<script setup>
  import { defineProps, ref } from "vue";
  import { useQuestionsStore } from "@/stores/questions";
  import Choice from "@/components/Choice.vue";

  const questionsStore = useQuestionsStore()


  const newText = ref("")
  const showForm = ref(false)
  const inputClass = ref([])
  const { questionId, choices } = defineProps(['questionId','choices'])


  function createItem() {
    if (!newText.value.toString().trim()) {
      inputClass.value = "required-field";
      return
    }
    questionsStore.createChoice(questionId, newText.value)
    newText.value = "";
    showForm.value = false;
    inputClass.value = "";
  }

</script>

<template>
  <div>
    <Choice v-for="item in choices" :question-id="questionId" :choice="item"></Choice>

    <div v-if="showForm">
      <input class="text" :class="inputClass" v-model="newText" />
      <button @click="createItem">Save</button>
    </div>
    <div>
      <button @click="showForm=true">Add choice</button>
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
