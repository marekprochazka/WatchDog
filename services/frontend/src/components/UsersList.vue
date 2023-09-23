<template>
  <div>
    <h1>Users {{ props.users }}</h1> jo

  </div>
</template>


<script setup lang="ts">
import type {IUsersListProps} from "@/components/props";

const props = defineProps<IUsersListProps>()
</script>