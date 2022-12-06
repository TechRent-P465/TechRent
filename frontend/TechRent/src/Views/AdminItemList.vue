<template>
  <div class="flex-table">
    <div>Name</div>
    <div>Description</div>
    <div>Actions</div>
  </div>
  <div v-for="item in items" :key="item.id" class="flex-table">
    <div>{{ item.item_name }}</div>
    <div>{{ item.description.slice(0, 50) + '...' }}</div>
    <div class="actions">
      <router-link :to="{ name: 'ItemPage', params: { id: item.id } }"
        >Review</router-link
      >
      <button @click="deleteItem(item)">Remove</button>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data() {
    return {
      items: [
        {
          id: 1,
          item_name: 'Mock item 1',
          description:
            'This is a long paragraph it consists of many mnay many words and many many many and many many manyand many many many and many many many and many many many and many many many and many many many'
        },
        {
          id: 2,
          item_name: 'Mock item 2',
          description:
            'This is a long paragraph it consists of many mnay many words and many many many and many many manyand many many many and many many many and many many many and many many many and many many many'
        },
        {
          id: 3,
          item_name: 'Mock item 3',
          description:
            'This is a long paragraph it consists of many mnay many words and many many many and many many manyand many many many and many many many and many many many and many many many and many many many'
        },
        {
          id: 4,
          item_name: 'Mock item 4',
          description:
            'This is a long paragraph it consists of many mnay many words and many many many and many many manyand many many many and many many many and many many many and many many many and many many many'
        }
      ]
    }
  },
  //   computed: {
  //     ...mapState(['items'])
  //   },
  methods: {
    deleteItem(item) {
      let response = confirm(`Are you sure you want to delete ${item.name}`)
      if (response) {
        this.$store.dispatch('deleteItem', item)
      }
    }
  }
}
</script>

<style scoped>
.flex-table {
  display: grid;
  grid-template-columns: repeat(auto-fill, 33%);
  padding: 10px;
  border-bottom: 1px black solid;
  /* &:nth-of-type(2n) {
    background-color: #dedede;
  } */
}
/* 
.actions {
    * {
      padding-right: 15px;
    }
  } */
</style>
