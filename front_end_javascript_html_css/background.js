// Create the right-click context menu
chrome.runtime.onInstalled.addListener(() => {
    chrome.contextMenus.create({
      id: "check-misinfo",
      title: "Check Misinformation",
      contexts: ["selection"]
    });
  });

// Handle the context menu click event
chrome.contextMenus.onClicked.addListener((info) => {
    chrome.storage.session.set({ selectedContent: info.selectionText });
    chrome.action.openPopup();
  });