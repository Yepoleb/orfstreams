import jinja2

CHANNELS = [
    ('orf1', 'ORF eins'),
    ('orf2', 'ORF 2'),
    ('orf3', 'ORF III'),
    ('web03', 'ORF SPORT +'),
    ('orf2b', 'ORF B'),
    ('orf2k', 'ORF K'),
    ('orf2n', 'ORF NÖ'),
    ('orf2ooe', 'ORF OÖ'),
    ('orf2s', 'ORF S'),
    ('orf2stmk', 'ORF St'),
    ('orf2t', 'ORF T'),
    ('orf2v', 'ORF V'),
    ('orf2w', 'ORF W')]

template = jinja2.Template(open("index_template.html").read())
channel_dicts = []

for channel in CHANNELS:
    channel_dict = {
        "id": channel[0],
        "name": channel[1]
    }
    channel_dicts.append(channel_dict)

index_file = open("index.html", "w")
index_file.write(template.render(channels=channel_dicts))
index_file.close()
