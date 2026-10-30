#pragma region template
// https://github.com/hotaru-ishibashi/python-library-atcoder/blob/main/cpp/cpp.cpp
#include <atcoder/all>
#include <bits/stdc++.h>
using namespace std;
using namespace atcoder;
using mint = static_modint<998244353>;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef std::pair<ll, ll> pll;
#define sz(a) static_cast<ll>(a.size())
#define rep(i, n) for(ll i = 0; i < (ll)(n); ++i)
#define rep1(i, n) for(ll i = 1; i <= (ll)(n); ++i)
#define rrep(i, n) for(ll i = (ll)(n) - 1; i >= 0; --i)
#define rrep1(i, n) for(ll i = (ll)(n); i >= 1; --i)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
const int dy[4] = {-1,0,1,0}; const int dx[4] = {0,1,0,-1};
const int dy8[8] = {-1,-1,-1,0,1,1,1,0}; const int dx8[8] = {-1,0,1,1,1,0,-1,-1};
const ll inf = 1000000000000000000;

template <class T>
istream& operator>>(istream& is, vector<T>& v) {
    for (auto& x : v) is >> x;
    return is;
}

template <class T>
void _print(const T& x);

template <class T, class U>
void _print(const pair<T, U>& p) {
    cerr << '(';
    _print(p.first);
    cerr << ", ";
    _print(p.second);
    cerr << ')';
}

template <class... Ts>
void _print(const tuple<Ts...>& t) {
    cerr << '(';
    size_t i = 0;
    apply([&](const auto&... xs) {
        ((cerr << (i++ ? ", " : ""), _print(xs)), ...);
    }, t);
    cerr << ')';
}

template <class T>
void _print(const T& x) {
    if constexpr (
        requires { x.begin(); x.end(); } &&
        !is_same_v<T, string>
    ) {
        cerr << '[';
        bool first = true;
        for (const auto& e : x) {
            if (!first) cerr << ", ";
            first = false;
            _print(e);
        }
        cerr << ']';
    } else {
        cerr << x;
    }
}

#define print(x) (cerr << #x << " = ", _print(x), cerr << '\n')

#pragma endregion

void solve() {
    // ll N, M; cin >> N >> M;
    // vector<ll> A(N); cin >> A;

    // ll ans = 0;
	// cout << ans << endl;
	return;
}

int main() {
	cin.tie(nullptr);
	ios::sync_with_stdio(false);
	int test_case = 1;
	// cin >> test_case;
	cout << std::setprecision(15);
	while(test_case--) {
		solve();
	}
	return 0;
}
