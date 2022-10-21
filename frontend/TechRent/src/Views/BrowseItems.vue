<template lang="">
  <div class="container">
    <div class="banner image-banner">
      <div class="banner-container">
        <div class="banner-section1">
          <h1>Browse Electronic Devices</h1>
          <h2>Search, filter, and locate items</h2>
        </div>
      </div>
    </div>
    <div class="content">
      <div class="items-container">
        <div class="search-container">
          <form action="" class="search-content">
            <input
              class="search-bar"
              type="text"
              v-model="search"
              placeholder="Search For Electronic Devices"
            />
            <button type="submit" class="search-button">
              <img src="../assets/search.png" class="my-icon" />
            </button>
          </form>
          <div class="filters">
            <div class="filter-container">
              <label for="filter-price">Price</label>
              <select id="filter-price" name="filter-price">
                <option value="-">------</option>
                <option value="low-high">low-high</option>
                <option value="high-low">high-low</option>
              </select>
            </div>
            <div class="filter-container">
              <label for="filter-device-type">Device Type</label>
              <select id="filter-device-type" name="filter-device-type">
                <option value="-">------</option>
                <option value="audio">audio</option>
                <option value="video">video</option>
                <option value="entertainment">entertainment</option>
                <option value=""></option>
              </select>
            </div>
          </div>
        </div>

        <div v-if="search" class="devices-container">
          <div class="devices-header">
            <h2>Searched Items</h2>
          </div>
          <div class="devices-content">
            <div
              v-for="device in filteredDevices"
              class="devices-item-container"
            >
              <Recommendation
                :ItemImage="device.image"
                :ItemName="device.name"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="map-container">
        <h1>Map will go here</h1>
      </div>
    </div>
  </div>
</template>
<script>
export default {}
</script>
<style>
/* Banner */
.image-banner {
  /*Photo by <a href="https://unsplash.com/@ollipexxer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Oliver Pecker</a> on <a href="https://unsplash.com/s/photos/technology?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>*/
  background-image: url(../assets/browse-banner.jpg);
  background-position: center center;
}

.image-banner h1 {
  color: var(--color-highlight);
  font-size: 40px;
}

.image-banner h2 {
  color: var(--color-highlight);
}

.banner-section1 {
  width: 100%;
  margin-bottom: 3em;
}

/* Content */
.content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin: 0 auto;
  padding: 0;
}

.items-container {
  width: 45%;
}

.map-container {
  width: 50%;
  border: 1px solid black;
  margin: 0;
  padding: 0;
}

/* filter */
.filters {
  display: flex;
}
.filter-container {
  display: flex;
  flex-direction: column;
  margin-right: 15px;
}

/* Devices */
.devices-item-container {
  margin: 0 15px 30px 0;
}

.devices-content {
  width: 100%;
  display: flex;
  align-items: center;
  flex-flow: row wrap;
}

/* Search */
.search-container {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.search-content {
  background-color: var(--color-highlight);
  box-shadow: inset 0 0 0 2000px rgba(62, 124, 177, 0.2);
  width: 80%;
  margin: 30px auto;
  height: 50px;
  border: 1px solid var(--color-pop);
  border-radius: 5px;
  display: flex;
  flex-direction: row;
  align-items: center;
  border-radius: 60px;
}
.my-icon {
  width: 30px;
  height: 30px;
}
.search-bar {
  background: transparent;
  outline: none;
  font-size: 20px;
  all: unset;
  width: 100%;
  height: 100%;
  padding: 10px;
}
.search-button {
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  background: transparent;
  margin-right: 10px;
}
</style>
