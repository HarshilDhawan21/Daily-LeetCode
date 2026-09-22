class Solution {
    static class Node {
        int pro = 1;
        int[] rest;
        Node(int k) { rest = new int[k]; }
    }
    int n, k;
    Node[] tree;
    public int[] resultArray(int[] nums, int k, int[][] queries) {
        this.n = nums.length;
        this.k = k;
        this.tree = new Node[4 * n];
        for (int i = 0; i < n; i++) nums[i] %= k;
        build(nums, 0, 0, n - 1);
        int[] ans = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int index = queries[q][0];
            int val = queries[q][1] % k;
            int start = queries[q][2];
            int a = queries[q][3];

            update(0, 0, n - 1, index, val);
            Node res = query(0, 0, n - 1, start, n - 1);
            ans[q] = res.rest[a];
        }
        return ans;
    }
    private void build(int[] nums, int node, int l, int r) {
        if (l == r) {
            tree[node] = new Node(k);
            tree[node].pro = nums[l];
            tree[node].rest[nums[l]] = 1;
            return;
        }
        int mid = (l + r) / 2;
        build(nums, 2 * node + 1, l, mid);
        build(nums, 2 * node + 2, mid + 1, r);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
    }
    private void update(int node, int l, int r, int i, int val) {
        if (l == r) {
            tree[node] = new Node(k);
            tree[node].pro = val;
            tree[node].rest[val] = 1;
            return;
        }
        int mid = (l + r) / 2;
        if (i <= mid) update(2 * node + 1, l, mid, i, val);
        else update(2 * node + 2, mid + 1, r, i, val);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
    }
    private Node query(int node, int l, int r, int i, int j) {
        if (i <= l && r <= j) return tree[node];
        int mid = (l + r) / 2;
        if (j <= mid) return query(2 * node + 1, l, mid, i, j);
        if (i > mid) return query(2 * node + 2, mid + 1, r, i, j);
        return merge(query(2 * node + 1, l, mid, i, j),
                     query(2 * node + 2, mid + 1, r, i, j));
    }
    private Node merge(Node left, Node right) {
        Node merged = new Node(k);
        merged.pro = (left.pro * right.pro) % k;
        for (int v = 0; v < k; v++) merged.rest[v] += left.rest[v];
        for (int v = 0; v < k; v++)
            if (right.rest[v] != 0)
                merged.rest[(v * left.pro) % k] += right.rest[v];
        return merged;
    }
}