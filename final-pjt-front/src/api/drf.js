const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'

export default {
  accounts: {
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
}
