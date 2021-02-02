// Generate a TOC for a directory of Markdown files
// The generated links point HTML files

const fs = require('fs');

const exclude = ['index'];

// Walk through the dir structure
// https://stackoverflow.com/a/59042581/7011476
function walk(dir, rootDir, level = 0) {
    let toc = '';
    let entry;
    rootDir = rootDir ? rootDir : dir;
    while ((entry = dir.readSync()) !== null) {
        if (entry.isDirectory()) {
            toc += `${'  '.repeat(level)}- ${entry.name}\n`;
            toc += walk(fs.opendirSync(dir.path + '/' + entry.name), rootDir, level + 1);
        } else if (entry.isFile && isMD(entry.name)) {
            const name = getName(entry.name);
            if (!exclude.includes(name)) {
                const dirPath = dir.path.slice(rootDir.path.length + 1);
                // - [name](path/to/name.html)
                toc += `${'  '.repeat(level)}- [${name}](${(dirPath ? dirPath + '/' : '') + name + '.html'})\n`;
            }
        }
    }
    return toc;
}

function isMD(fileName) {
    const splits = fileName.split('.');
    if (splits.length <= 1) {
        return false;
    }
    const ext = splits[splits.length - 1];
    return ['md', 'markdown'].includes(ext);
}

// Get file name without the extension
function getName(md) {
    const splits = md.split('.');
    return splits.slice(0, splits.length - 1).join('.');
}


let [, , rootDir, outputFile, fileTitle, verbose] = process.argv;
rootDir = fs.opendirSync(rootDir ? rootDir : './');
console.log(`Generating TOC for directory "${rootDir.path}".`);
const toc = walk(rootDir);
if (verbose) console.log(toc);
if (outputFile) {
    console.log(`Writing TOC to "${outputFile}".`)
    if (fileTitle) {
        fs.writeFileSync(outputFile, '# ' + fileTitle + '\n\n' + toc)
    } else {
        fs.writeFileSync(outputFile, toc);
    }
}
