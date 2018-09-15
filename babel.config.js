module.exports = {
    presets: [
        ['@babel/preset-env', {
            "targets": "> 1%"
        }],
        '@babel/preset-react'
    ],
    plugins: [
        '@babel/plugin-syntax-dynamic-import',
        '@babel/plugin-proposal-class-properties'
    ]
};
